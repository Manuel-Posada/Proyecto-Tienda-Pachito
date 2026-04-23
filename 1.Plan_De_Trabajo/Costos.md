# Estimación de Costos — Sistema de Gestión Tienda Pachito
**Método:** Story Points (Secuencia de Fibonacci) + Conversión a horas y COP  
**Proyecto:** Sistema básico de gestión para tienda local Pachito  
**Equipo:** 4 personas (Product Owner, Scrum Master, 2 Developers)  
**Sprints:** 3 sprints de 2 semanas cada uno (6 semanas totales)

---

## 1. Criterios de estimación

| Story Points | Significado | Ejemplo |
|:---:|---|---|
| 1 | Tarea trivial, menos de 1 hora | Ajuste de texto o validación simple |
| 2 | Tarea simple, ~2 horas | Formulario básico sin lógica |
| 3 | Tarea estándar, ~4 horas | CRUD completo de una entidad |
| 5 | Tarea media, ~8 horas | Módulo con lógica de negocio |
| 8 | Tarea compleja, ~16 horas | Módulo con múltiples integraciones |
| 13 | Tarea muy compleja, ~24 horas | Módulo crítico con pruebas extensas |

**Conversión base:**  
- Developer Junior: **1 SP = 2 horas**  
- Basado en salario Junior Colombia: **$8.40 USD/hora ≈ $34.000 COP/hora** (TRM ~$4.050)

---

## 2. Estimación por Historia de Usuario

### 🔵 Sprint 1 — Prioridad Alta

#### PB-01 — Registro de Productos

| ID | Tarea | SP |
|---|---|:---:|
| T1 | Diseñar tabla Productos en base de datos | 2 |
| T2 | Crear modelo Producto | 2 |
| T3 | Crear formulario de registro de producto | 3 |
| T4 | Implementar guardado en base de datos | 3 |
| T5 | Implementar edición de precio | 2 |
| T6 | Validar campos obligatorios | 1 |
| T7 | Pruebas de registro y edición | 2 |
| **Total PB-01** | | **15 SP** |

#### PB-02 — Registro rápido de ventas

| ID | Tarea | SP |
|---|---|:---:|
| T8 | Diseñar tabla Ventas | 2 |
| T9 | Crear interfaz de selección de productos | 3 |
| T10 | Implementar ingreso de cantidad vendida | 2 |
| T11 | Programar cálculo automático del total | 3 |
| T12 | Guardar venta en base de datos | 2 |
| T13 | Validar cantidades ingresadas | 1 |
| T14 | Pruebas de registro de ventas | 2 |
| **Total PB-02** | | **15 SP** |

#### PB-03 — Actualización automática de stock

| ID | Tarea | SP |
|---|---|:---:|
| T15 | Implementar descuento automático de stock | 5 |
| T16 | Mostrar stock actualizado en pantalla | 2 |
| T17 | Validar disponibilidad antes de vender | 3 |
| T18 | Mostrar mensaje de stock insuficiente | 1 |
| T19 | Pruebas de actualización de inventario | 3 |
| **Total PB-03** | | **14 SP** |

> **Total Sprint 1: 44 SP**

---

### 🟡 Sprint 2 — Prioridad Media

#### PB-04 — Registro de compras a proveedores

| ID | Tarea | SP |
|---|---|:---:|
| T20 | Diseñar tabla Compras en base de datos | 2 |
| T21 | Crear interfaz de selección de producto a comprar | 3 |
| T22 | Implementar suma automática al stock | 5 |
| T23 | Guardar fecha de compra | 1 |
| T24 | Pruebas de registro de compras | 2 |
| **Total PB-04** | | **13 SP** |

#### PB-05 — Reporte diario automático

| ID | Tarea | SP |
|---|---|:---:|
| T25 | Calcular total vendido del día | 5 |
| T26 | Mostrar número de productos vendidos | 3 |
| T27 | Implementar filtro por fecha | 5 |
| T28 | Generar resumen visual claro | 3 |
| T29 | Pruebas de generación de reportes | 3 |
| **Total PB-05** | | **19 SP** |

> **Total Sprint 2: 32 SP**

---

### 🟢 Sprint 3 — Prioridad Baja

#### PB-06 — Alerta de stock bajo

| ID | Tarea | SP |
|---|---|:---:|
| T30 | Crear configuración de stock mínimo por producto | 3 |
| T31 | Implementar lógica de evaluación de mínimo | 5 |
| T32 | Mostrar alerta visual en pantalla | 3 |
| T33 | Guardar configuración en base de datos | 2 |
| T34 | Pruebas de alerta de stock | 2 |
| **Total PB-06** | | **15 SP** |

> **Total Sprint 3: 15 SP**

---

## 3. Resumen de Story Points por Sprint

| Sprint | Historias | Story Points | % del proyecto |
|---|---|:---:|:---:|
| Sprint 1 | PB-01, PB-02, PB-03 | 44 SP | 48% |
| Sprint 2 | PB-04, PB-05 | 32 SP | 35% |
| Sprint 3 | PB-06 | 15 SP | 16% |
| **TOTAL** | **6 historias** | **91 SP** | **100%** |

---

## 4. Conversión a horas y costos en COP

### Supuestos
- 1 SP = 2 horas de trabajo (perfil Junior, equipo universitario)
- Tarifa hora Junior Colombia: **$34.000 COP/hora**
- TRM referencia: $4.050 COP por USD
- Equipo de desarrollo: **2 Developers**
- Duración sprint: 2 semanas (10 días hábiles, 6 horas/día efectivas)

### Cálculo de horas y costo por sprint

| Sprint | SP | Horas totales | Horas por developer | Costo/hora | Costo total |
|---|:---:|:---:|:---:|---|---|
| Sprint 1 | 44 | 88 horas | 44 horas | $34.000 | **$2.992.000 COP** |
| Sprint 2 | 32 | 64 horas | 32 horas | $34.000 | **$2.176.000 COP** |
| Sprint 3 | 15 | 30 horas | 15 horas | $34.000 | **$1.020.000 COP** |
| **TOTAL** | **91** | **182 horas** | **91 horas c/u** | | **$6.188.000 COP** |

---

## 5. Estimación de precio al cliente (con margen de ganancia)

Para un proyecto real se aplica un margen sobre el costo base para cubrir imprevistos, herramientas y ganancia:

| Concepto | Valor |
|---|---|
| Costo base del equipo | $6.188.000 COP |
| Margen de imprevistos (15%) | $928.200 COP |
| Margen de ganancia (20%) | $1.237.600 COP |
| **Precio estimado al cliente** | **$8.353.800 COP** |
| **Precio redondeado al cliente** | **~$8.400.000 COP** |

---

## 6. Cronograma estimado

| Sprint | Semanas | Fechas estimadas | Entregable |
|---|:---:|---|---|
| Sprint 1 | 2 semanas | Semana 1 – Semana 2 | Registro productos, ventas y stock |
| Sprint 2 | 2 semanas | Semana 3 – Semana 4 | Compras y reportes |
| Sprint 3 | 2 semanas | Semana 5 – Semana 6 | Alertas de stock |
| **Total** | **6 semanas** | | **Sistema completo** |

---

## 7. Velocidad del equipo

La velocidad es la cantidad de SP que el equipo completa por sprint:

| Sprint | SP completados | Velocidad |
|---|:---:|---|
| Sprint 1 | 44 SP | Alta (funcionalidades críticas) |
| Sprint 2 | 32 SP | Media (módulos de soporte) |
| Sprint 3 | 15 SP | Baja (mejoras opcionales) |
| **Promedio** | **~30 SP/sprint** | |

> **Nota:** La velocidad disminuye progresivamente porque los sprints posteriores tienen menos historias pero con mayor complejidad de integración.

---

*Estimación realizada con el método Story Points usando secuencia de Fibonacci.*  
*Tarifa basada en salario promedio desarrollador Junior Colombia (2025).*  
*Universidad de Ibagué — Ingeniería de Software I — Grupo 02*
