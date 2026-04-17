# 📋 Requisitos No Funcionales – Tienda Pachito

**Proyecto:** Sistema básico de gestión para tienda local Pachito
**Tecnología:** Python · SQLite
**Product Owner:** Ángel Antonio Suárez Vera
**Scrum Master:** Manuel Alejandro Posada Zartha
**Development Team:** Wilson Alejandro Céspedes Alarcón, David Felipe Lucero Trujillo

---

## ⚡ Rendimiento

### RNF-01 – Tiempo de respuesta
**Descripción:** El sistema debe responder a cualquier operación (registro, consulta, venta) en menos de 2 segundos.

**Criterios de aceptación:**
- Registro de venta: < 2 s
- Consulta de stock: < 1 s
- Generación de reporte diario: < 3 s

**Prioridad:** Alta

---

### RNF-02 – Uso de recursos
**Descripción:** El sistema debe funcionar correctamente en equipos de bajas especificaciones, típicos de una tienda local.

**Criterios de aceptación:**
- RAM mínima: 2 GB
- Procesador: 1 GHz o superior
- Sin necesidad de conexión a internet

**Prioridad:** Alta

---

## 🖥️ Usabilidad

### RNF-03 – Facilidad de uso
**Descripción:** La interfaz debe ser comprensible para usuarios sin conocimientos técnicos, como el dueño o empleados de la tienda.

**Criterios de aceptación:**
- Menú principal con máximo 5 opciones visibles
- Iconos o etiquetas claras en cada función
- Usuario nuevo opera el sistema en < 10 minutos

**Prioridad:** Alta

---

### RNF-04 – Mensajes de error claros
**Descripción:** El sistema debe mostrar mensajes de error comprensibles cuando el usuario cometa una acción incorrecta.

**Criterios de aceptación:**
- Mensaje en español, sin tecnicismos
- Indica qué campo está incorrecto
- No permite guardar datos inválidos silenciosamente

**Prioridad:** Media

---

## 🔒 Seguridad

### RNF-05 – Protección de datos
**Descripción:** Los datos de ventas, productos e inventario deben estar protegidos contra modificaciones accidentales o no autorizadas.

**Criterios de aceptación:**
- La base de datos no debe ser accesible directamente por el usuario
- Solo el sistema modifica los registros vía la aplicación

**Prioridad:** Alta

---

### RNF-06 – Integridad de datos
**Descripción:** El sistema debe garantizar que no se registren datos duplicados o inconsistentes (p.ej., stock negativo).

**Criterios de aceptación:**
- Validación antes de guardar
- El stock nunca puede quedar en valor negativo
- Precios y cantidades solo aceptan valores positivos

**Prioridad:** Alta

---

## 🔧 Mantenibilidad

### RNF-07 – Código modular
**Descripción:** El código Python debe estar organizado en módulos separados por funcionalidad para facilitar cambios futuros.

**Criterios de aceptación:**
- Módulo separado para productos, ventas, compras y reportes
- Funciones documentadas con comentarios

**Prioridad:** Media

---

### RNF-08 – Base de datos organizada
**Descripción:** La base de datos debe tener una estructura clara y normalizada para facilitar consultas y futuras ampliaciones.

**Criterios de aceptación:**
- Tablas separadas: productos, ventas, compras
- Uso de claves foráneas
- Sin redundancia de datos

**Prioridad:** Media

---

## 🟢 Disponibilidad

### RNF-09 – Funcionamiento offline
**Descripción:** El sistema debe funcionar completamente sin conexión a internet, ya que la tienda puede no tener acceso continuo.

**Criterios de aceptación:**
- Toda la lógica y datos son locales
- No depende de servicios en la nube

**Prioridad:** Alta

---

### RNF-10 – Recuperación ante fallos
**Descripción:** Si el sistema se cierra inesperadamente, los datos ya guardados no deben perderse.

**Criterios de aceptación:**
- Uso de transacciones en la base de datos (SQLite)
- Datos confirmados antes de cerrar la operación

**Prioridad:** Alta

---

## 🌐 Portabilidad

### RNF-11 – Compatibilidad con sistemas operativos
**Descripción:** El sistema debe poder ejecutarse en Windows, que es el SO más común en tiendas locales de Colombia.

**Criterios de aceptación:**
- Compatible con Windows 10 o superior
- Ejecutable sin instalación compleja (Python + dependencias)

**Prioridad:** Media

---

## 📊 Resumen

| ID     | Nombre                            | Categoría       | Prioridad |
|--------|-----------------------------------|-----------------|-----------|
| RNF-01 | Tiempo de respuesta               | Rendimiento     | Alta      |
| RNF-02 | Uso de recursos                   | Rendimiento     | Alta      |
| RNF-03 | Facilidad de uso                  | Usabilidad      | Alta      |
| RNF-04 | Mensajes de error claros          | Usabilidad      | Media     |
| RNF-05 | Protección de datos               | Seguridad       | Alta      |
| RNF-06 | Integridad de datos               | Seguridad       | Alta      |
| RNF-07 | Código modular                    | Mantenibilidad  | Media     |
| RNF-08 | Base de datos organizada          | Mantenibilidad  | Media     |
| RNF-09 | Funcionamiento offline            | Disponibilidad  | Alta      |
| RNF-10 | Recuperación ante fallos          | Disponibilidad  | Alta      |
| RNF-11 | Compatibilidad con SO             | Portabilidad    | Media     |

**Total:** 11 requisitos no funcionales · 6 categorías · Prioridad alta: 7 · Prioridad media: 4
