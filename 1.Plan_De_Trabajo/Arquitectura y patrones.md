# 🏗️ Arquitectura y Patrones Utilizados

## 🔹 Descripción General

El sistema de la tienda **Pachito** fue desarrollado utilizando una arquitectura **cliente-servidor**, complementada con distintos patrones de diseño que permiten mejorar la organización, escalabilidad y mantenibilidad del proyecto.

Esta combinación permite separar responsabilidades entre el frontend y el backend, facilitando el desarrollo y futuras mejoras.

---

## 🔹 ¿Por qué Cliente-Servidor?

Se eligió la arquitectura cliente-servidor porque permite dividir el sistema en dos partes principales:

- **Cliente (Frontend - Angular):** Encargado de la interfaz de usuario  
- **Servidor (Backend - Django):** Encargado de la lógica de negocio y acceso a datos  

### ✅ Ventajas en el proyecto:

- Separación clara de responsabilidades  
- Posibilidad de escalar frontend y backend de forma independiente  
- Mayor seguridad al centralizar la lógica en el servidor  
- Facilita el mantenimiento y actualización del sistema  
- Permite reutilizar el backend (por ejemplo, con apps móviles en el futuro)  

---

## 🔹 Patrones Arquitectónicos Aplicados

A continuación se describen los patrones utilizados en el proyecto y la razón de su implementación:

---

### 🟢 Singleton

**Uso:** Servicios como `ApiService` y `ToastService`

**¿Por qué se utilizó?**

Se garantiza que exista una única instancia de estos servicios en toda la aplicación, evitando duplicación de lógica y asegurando un manejo centralizado de:

- Peticiones HTTP  
- Notificaciones al usuario  

---

### 🔵 Prototype

**Uso:** Método `copy()` en manejo de datos

**¿Por qué se utilizó?**

Permite crear copias de objetos sin modificar los originales, lo cual es útil para:

- Evitar efectos secundarios en los datos  
- Manipular información temporalmente (formularios, ediciones)  

---

### 🟡 Facade

**Uso:** `ApiService` como punto de acceso al backend

**¿Por qué se utilizó?**

Simplifica la comunicación con el servidor ocultando la complejidad de las peticiones HTTP.

Esto permite que otros componentes:

- No necesiten saber cómo se hacen las peticiones  
- Usen métodos simples como `get()`, `post()`, etc.  

---

### 🟠 Proxy

**Uso:** `proxy.conf.json` en Angular

**¿Por qué se utilizó?**

Actúa como intermediario entre el frontend y el backend, permitiendo:

- Evitar problemas de CORS  
- Redirigir automáticamente las peticiones a `/api`  
- Simular un entorno de producción en desarrollo  

---

### 🟣 Decorator

**Uso:** `@Component`, `@Injectable`, `@Pipe`

**¿Por qué se utilizó?**

Permite agregar funcionalidades a clases sin modificarlas directamente.

En Angular se utiliza para:

- Definir componentes  
- Inyectar dependencias  
- Transformar datos en la vista  

---

### 🟤 Composite

**Uso:** Estructura de componentes anidados en Angular

**¿Por qué se utilizó?**

Permite construir interfaces complejas a partir de componentes pequeños y reutilizables.

Esto facilita:

- Reutilización de código  
- Organización de la UI  
- Escalabilidad del frontend  

---

### 🔴 Observer

**Uso:** `Observable`, `subscribe()` y `signal()`

**¿Por qué se utilizó?**

Permite reaccionar automáticamente a cambios en los datos.

Se utiliza para:

- Manejar peticiones HTTP  
- Actualizar la interfaz en tiempo real  
- Gestionar eventos  

---

### ⚫ Strategy

**Uso:** Enrutamiento con lazy loading

**¿Por qué se utilizó?**

Permite cambiar el comportamiento del sistema dinámicamente.

En este caso:

- Cargar módulos según la ruta  
- Optimizar el rendimiento de la aplicación  

---

### ⚪ Iterator

**Uso:** Directiva `*ngFor`

**¿Por qué se utilizó?**

Permite recorrer colecciones de datos de forma sencilla en la vista.

Facilita:

- Mostrar listas de productos  
- Renderizar datos dinámicamente  

---

### 🔵 Command

**Uso:** Métodos como `guardar()` y `eliminar()`

**¿Por qué se utilizó?**

Encapsula acciones como operaciones independientes.

Esto permite:

- Reutilizar lógica  
- Desacoplar acciones de la interfaz  

---

### 🟢 State

**Uso:** `signal()` para manejo de estado

**¿Por qué se utilizó?**

Permite controlar el estado de la interfaz de usuario de forma reactiva.

Se utiliza para:

- Actualizar vistas automáticamente  
- Manejar cambios en datos sin recargar la página  

---

## 🎯 Objetivo

El uso de esta arquitectura y patrones tiene como objetivo:

- Mejorar la organización del sistema  
- Reducir el acoplamiento entre componentes  
- Facilitar el mantenimiento y escalabilidad  
- Optimizar el rendimiento del frontend  
- Aplicar buenas prácticas de desarrollo  

De esta manera, el sistema de la tienda Pachito se construye como una solución robusta, modular y preparada para futuras mejoras.