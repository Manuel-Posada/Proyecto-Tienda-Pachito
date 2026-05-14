# 🧱 Aplicación de Principios SOLID

## 🔹 Descripción General

En el desarrollo del sistema para la tienda **Pachito**, se aplican los principios **SOLID**, los cuales son un conjunto de buenas prácticas de diseño orientadas a crear software más mantenible, escalable y fácil de entender.

Estos principios permiten estructurar el código de forma que sea más flexible ante cambios, evitando errores comunes como el acoplamiento excesivo o la duplicación de lógica.

---

## 🔹 ¿Qué es SOLID?

SOLID es un acrónimo que representa cinco principios fundamentales de la programación orientada a objetos:

- **S** – Single Responsibility Principle (Responsabilidad única)  
- **O** – Open/Closed Principle (Abierto/Cerrado)  
- **L** – Liskov Substitution Principle (Sustitución de Liskov)  
- **I** – Interface Segregation Principle (Segregación de interfaces)  
- **D** – Dependency Inversion Principle (Inversión de dependencias)  

Cada uno de estos principios contribuye a mejorar la calidad del software.

---

## 🔹 Aplicación en el Proyecto

### 🟢 Single Responsibility Principle

Cada clase del sistema tiene una única responsabilidad.

Por ejemplo:

- Las clases de **modelo** representan únicamente los datos (Producto, Venta)  
- Los **servicios** manejan la lógica de negocio (cálculos, validaciones)  
- Los **controladores** gestionan las solicitudes del usuario  

Esto permite que los cambios en una funcionalidad no afecten otras partes del sistema.

---

### 🔵 Open/Closed Principle 

El sistema está diseñado para permitir agregar nuevas funcionalidades sin modificar el código existente.

Por ejemplo:

- Se pueden agregar nuevos métodos de pago sin cambiar la lógica principal  
- Es posible extender funcionalidades como tipos de reporte o promociones  

Esto se logra mediante el uso de clases base y herencia.

---

### 🟡 Liskov Substitution Principle 

Las clases hijas pueden reemplazar a las clases padre sin alterar el funcionamiento del sistema.

Por ejemplo:

- Un tipo de usuario como **Cliente** puede usarse en lugar de un **Usuario** sin generar errores  
- Se evita que las clases hijas implementen comportamientos que no les corresponden  

Esto garantiza coherencia en el diseño del sistema.

---

### 🟠 Interface Segregation Principle

Se evita obligar a las clases a implementar métodos que no necesitan.

Por ejemplo:

- Un usuario tipo **Empleado** no tiene acceso a funciones administrativas  
- Las funcionalidades se dividen según el rol del usuario  

Esto hace el sistema más claro y reduce dependencias innecesarias.

---

### 🔴 Dependency Inversion Principle

Las clases dependen de abstracciones y no de implementaciones concretas.

Por ejemplo:

- Un módulo de pedidos no depende directamente de un método de pago específico  
- Se pueden cambiar implementaciones (como pago en efectivo o tarjeta) sin afectar el sistema  

Esto facilita la escalabilidad y el mantenimiento del proyecto.

---

## 🔹 Beneficios en el Proyecto

La aplicación de SOLID en el sistema de la tienda Pachito permite:

- Reducir el acoplamiento entre componentes  
- Facilitar la incorporación de nuevas funcionalidades  
- Mejorar la organización del código  
- Hacer el sistema más fácil de mantener  
- Reducir errores en futuras modificaciones  

---

## 🔹 Estructura del Sistema

El proyecto se organiza en diferentes capas siguiendo estos principios:

- **Modelos:** Representan los datos del sistema  
- **Servicios:** Contienen la lógica de negocio  
- **Controladores:** Manejan la interacción con el usuario  
- **Interfaces:** Definen comportamientos generales  
- **Repositorios:** Gestionan el acceso a la base de datos  

Esta separación permite que cada parte del sistema cumpla una función específica.

---

## 🎯 Objetivo

El uso de los principios SOLID en el proyecto tiene como objetivo:

- Desarrollar un sistema más organizado y escalable  
- Facilitar el trabajo en equipo  
- Permitir cambios sin afectar todo el sistema  
- Garantizar buenas prácticas de desarrollo  

De esta manera, se construye una solución robusta y preparada para futuras mejoras en la tienda Pachito.