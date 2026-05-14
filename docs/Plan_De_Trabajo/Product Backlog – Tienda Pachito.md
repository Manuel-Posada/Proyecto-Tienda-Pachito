# 🛒 Product Backlog – Tienda Pachito

**Proyecto:** Sistema básico de gestión para tienda local Pachito  
**Product Owner:** Ángel Antonio Suárez Vera  
**Scrum Master:** Manuel Alejandro Posada Zartha  
**Development Team:** Wilson Alejandro Cespedes Alarcón, David Felipe Lucero Trujillo  

---

## 🔴 Prioridad Alta

### 🔹 PB-01 – Registro de Productos
**Historia de usuario:**  
Como dueño de la tienda, quiero registrar los productos con su nombre, precio y cantidad inicial, para evitar errores al recordar precios de memoria.

**Criterios de aceptación:**
- Permite agregar nombre del producto  
- Permite ingresar precio  
- Permite ingresar cantidad inicial  
- Guarda la información en la base de datos  
- Permite editar precio  

**Valor de negocio:** Alto  

---

### 🔹 PB-02 – Registro de Ventas
**Historia de usuario:**  
Como empleado, quiero registrar una venta seleccionando el producto e ingresando la cantidad vendida, para agilizar el proceso de atención.

**Criterios de aceptación:**
- Permite seleccionar producto  
- Permite ingresar cantidad  
- Calcula automáticamente el total  
- Guarda la venta  

**Valor de negocio:** Alto  

---

### 🔹 PB-03 – Actualización de Stock
**Historia de usuario:**  
Como dueño, quiero que el sistema actualice automáticamente el inventario, para conocer el stock en tiempo real.

**Criterios de aceptación:**
- Descuenta automáticamente el stock  
- Muestra stock actualizado  
- Bloquea ventas sin stock  

**Valor de negocio:** Crítico  

---

## 🟡 Prioridad Media

### 🔹 PB-04 – Registro de Compras
**Historia de usuario:**  
Como dueño, quiero registrar compras de productos, para mantener actualizado el inventario.

**Criterios de aceptación:**
- Permite seleccionar producto  
- Permite ingresar cantidad  
- Suma automáticamente al stock  
- Guarda fecha  

**Valor de negocio:** Alto  

---

### 🔹 PB-05 – Reporte Diario
**Historia de usuario:**  
Como dueño, quiero visualizar el total vendido al día, para conocer mis ingresos.

**Criterios de aceptación:**
- Muestra total vendido  
- Muestra cantidad de productos  
- Permite filtrar por fecha  
- Genera resumen  

**Valor de negocio:** Alto  

---

## 🟢 Prioridad Baja

### 🔹 PB-06 – Alerta de Stock Bajo
**Historia de usuario:**  
Como dueño, quiero recibir alertas de stock bajo, para reabastecer a tiempo.

**Criterios de aceptación:**
- Permite definir mínimo de stock  
- Genera alerta visual  

**Valor de negocio:** Medio  

---

# 🚀 Plan de Sprints

## Sprint 1
- PB-01 Registro de productos  
- PB-02 Registro de ventas  
- PB-03 Actualización de stock  

## Sprint 2
- PB-04 Registro de compras  
- PB-05 Reporte diario  

## Sprint 3
- PB-06 Alertas  

---

# 🎯 Justificación Estratégica

Este backlog se enfoca en:

- Reducir errores humanos  
- Automatizar procesos manuales  
- Mejorar el control del inventario  
- Ahorrar tiempo operativo  

No se incluye gestión de clientes porque no aporta valor inmediato al negocio.

---
