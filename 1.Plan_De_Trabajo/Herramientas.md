# 🛠️ Herramientas del Proyecto

## 🔹 Backend – Python con Django

Para el desarrollo del backend se utilizará **Python** junto con el framework **Django**.

**¿Por qué Django?**

- Permite desarrollar aplicaciones web de forma rápida gracias a su estructura ya definida  
- Incluye funcionalidades integradas como autenticación, manejo de base de datos y panel administrativo  
- Facilita la conexión con bases de datos mediante su ORM (Object Relational Mapping)  
- Reduce la cantidad de código necesario, lo que acelera el desarrollo del proyecto  

**Relación con el proyecto:**

Django será el encargado de gestionar toda la lógica del sistema, incluyendo:

- Registro de productos  
- Procesamiento de ventas  
- Actualización automática del stock  
- Manejo de datos en la base de datos  

Esto lo convierte en una herramienta ideal para garantizar la correcta funcionalidad del sistema de gestión de la tienda.

---

## 🔹 Frontend – Angular

Para el desarrollo del frontend se utilizará el framework **Angular**.

**¿Por qué Angular?**

- Permite crear interfaces dinámicas y modernas  
- Facilita la organización del código mediante componentes  
- Mejora la experiencia del usuario con aplicaciones rápidas y reactivas  
- Se integra fácilmente con APIs, como las que se desarrollarán en Django  

**Relación con el proyecto:**

Angular se encargará de toda la interacción con el usuario, permitiendo:

- Registrar productos mediante formularios  
- Visualizar el inventario en tiempo real  
- Registrar ventas de manera rápida  
- Mostrar reportes y resúmenes de información  

Esto asegura una interfaz clara, intuitiva y eficiente para el uso diario de la tienda.

---

## 🔹 Base de Datos – MySQL Workbench

Para la gestión de la base de datos se utilizará **MySQL Workbench**.

**¿Por qué MySQL Workbench?**

- Permite diseñar y administrar bases de datos de manera visual  
- Facilita la creación de tablas, relaciones y consultas SQL  
- Es compatible con MySQL, una de las bases de datos más utilizadas  
- Permite monitorear y administrar el estado de la base de datos  

**Relación con el proyecto:**

MySQL Workbench será utilizado para:

- Crear la estructura de la base de datos (tablas de productos, ventas, etc.)  
- Gestionar las relaciones entre los datos  
- Ejecutar consultas para validar información  
- Administrar el almacenamiento de datos del sistema  

Esto garantiza un manejo eficiente y organizado de toda la información de la tienda.

---

## 🔗 Integración de Tecnologías

La arquitectura del proyecto estará basada en la separación entre frontend y backend:

- **Django** funcionará como API, gestionando la lógica y los datos  
- **Angular** consumirá esta API para mostrar la información al usuario  
- **MySQL** almacenará toda la información del sistema, administrado mediante MySQL Workbench  

**Beneficios de esta arquitectura:**

- Mayor organización del proyecto  
- Escalabilidad a futuro  
- Posibilidad de reutilizar el backend con otras aplicaciones  
- Desarrollo independiente entre frontend y backend  

---

## 🎯 Justificación General

La combinación de Django, Angular y MySQL permite construir un sistema:

- Robusto y seguro  
- Fácil de mantener  
- Escalable  
- Adaptado a las necesidades del negocio  

Estas herramientas fueron seleccionadas porque se ajustan perfectamente a los requerimientos del sistema de gestión de la tienda Pachito, permitiendo desarrollar una solución eficiente y funcional.