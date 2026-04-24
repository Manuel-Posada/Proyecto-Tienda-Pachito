import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../core/services/api.service';
import { ToastService } from '../../core/services/toast.service';
import { Producto } from '../../core/models/models';
import { CopPipe } from '../../shared/pipes/cop.pipe';

@Component({
  selector: 'app-inventario',
  standalone: true,
  imports: [CommonModule, FormsModule, CopPipe],
  templateUrl: './inventario.component.html',
  styleUrls: ['./inventario.component.scss']
})
export class InventarioComponent implements OnInit {
  productos = signal<Producto[]>([]);
  mostrarModal = signal(false);
  modoEdicion = signal(false);
  cargando = signal(false);

  emojis = ['🍞','🥛','🍎','🌾','🫙','🥚','🧃','🧈','🍗','🥩','🐟','🍅','🥕','🧄','🧅','☕','🍫','🧂','📦','🛒'];

  form = {
    id: 0,
    nombre: '',
    precio: 0,
    stock: 0,
    stock_minimo: 10,
    emoji: '📦'
  };

  constructor(private api: ApiService, private toast: ToastService) {}

  ngOnInit() { this.cargar(); }

  cargar() {
    this.cargando.set(true);
    this.api.getProductos().subscribe({
      next: p => { this.productos.set(p); this.cargando.set(false); },
      error: () => { this.toast.mostrar('Error al cargar productos', 'error'); this.cargando.set(false); }
    });
  }

  abrirNuevo() {
    this.form = { id: 0, nombre: '', precio: 0, stock: 0, stock_minimo: 10, emoji: '📦' };
    this.modoEdicion.set(false);
    this.mostrarModal.set(true);
  }

  abrirEdicion(p: Producto) {
    this.form = { ...p };
    this.modoEdicion.set(true);
    this.mostrarModal.set(true);
  }

  cerrarModal() { this.mostrarModal.set(false); }

  guardar() {
    if (!this.form.nombre || this.form.precio <= 0) {
      this.toast.mostrar('Nombre y precio son obligatorios', 'error');
      return;
    }
    if (this.modoEdicion()) {
      this.api.actualizarProducto(this.form.id, this.form).subscribe({
        next: () => { this.toast.mostrar('Producto actualizado'); this.cerrarModal(); this.cargar(); },
        error: () => this.toast.mostrar('Error al actualizar', 'error')
      });
    } else {
      this.api.crearProducto(this.form).subscribe({
        next: () => { this.toast.mostrar('Producto agregado'); this.cerrarModal(); this.cargar(); },
        error: () => this.toast.mostrar('Error al crear producto', 'error')
      });
    }
  }

  eliminar(p: Producto) {
    if (!confirm(`¿Eliminar "${p.nombre}"?`)) return;
    this.api.eliminarProducto(p.id).subscribe({
      next: () => { this.toast.mostrar('Producto eliminado', 'alerta'); this.cargar(); },
      error: () => this.toast.mostrar('Error al eliminar', 'error')
    });
  }

  stockClass(p: Producto): string {
    if (p.stock === 0) return 'stock--empty';
    if (p.stock <= p.stock_minimo) return 'stock--low';
    return 'stock--ok';
  }
}
