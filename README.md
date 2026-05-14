# 🛒 Proyecto Tienda Pachito

Sistema de gestión para la administración de una tienda local, enfocado en mejorar el control de inventario, registro de ventas y generación de reportes.

## 🌐 Aplicación desplegada

https://tienda-pachito-app-production.up.railway.app/dashboard

---

# 📌 Descripción

Proyecto desarrollado para optimizar la administración de una tienda mediante la automatización de procesos como:

* 📦 Gestión de inventario
* 💰 Registro de ventas
* 🛒 Venta de múltiples productos mediante carrito
* 🧾 Generación automática de recibos
* 📊 Reportes de ventas
* 🏪 Registro de compras a proveedores
* ⚠️ Alertas de stock bajo

El sistema busca reducir errores manuales, mejorar el control del negocio y facilitar la administración diaria.

---

# 🚀 Mejoras recientes

## ✅ Nuevas funcionalidades implementadas

* 🧾 Generación automática de recibos para ventas recientes
* 🛒 Carrito de compras para registrar múltiples productos en una sola venta
* 🔊 Sonidos interactivos en botones y diferentes acciones de la aplicación
* 🔍 Barra de búsqueda de productos en el menú de ventas
* 📜 Barra de desplazamiento en el inventario dentro de nueva venta
* 🔎 Barra de búsqueda en inventario

Estas mejoras fueron enfocadas en mejorar la experiencia de usuario, usabilidad y mantenimiento del sistema.

---

# 🎯 Objetivo del sistema

Optimizar la administración del negocio mediante la automatización de procesos clave, mejorando la precisión de los datos y facilitando la toma de decisiones.

---

# 🧠 Metodología de desarrollo

El proyecto se desarrolla utilizando la metodología ágil **Scrum**, organizando el trabajo mediante:

* 📋 Product Backlog
* 👤 Historias de Usuario
* 🗺️ Story Map
* 📅 Actas de reuniones
* 📄 Requisitos funcionales y no funcionales
* 📐 Diagramas UML y de arquitectura

---

# 👥 Equipo de trabajo

* **Product Owner:** Ángel Antonio Suárez Vera
* **Scrum Master:** Manuel Alejandro Posada Zartha
* **Development Team:**

  * Wilson Alejandro Cespedes Alarcón
  * David Felipe Lucero Trujillo

---

# 🧩 Historias de Usuario

* **HU-01:** Registro de productos
* **HU-02:** Registro de ventas
* **HU-03:** Actualización automática de stock
* **HU-04:** Registro de compras a proveedores
* **HU-05:** Reporte diario de ventas
* **HU-06:** Alerta de stock bajo

---

# 🗂️ Estructura del repositorio

```bash
Proyecto-Tienda-Pachito/
│
├── docs/
│   ├── DiagramasUML/
│   ├── Diagramas_Arquitectura/
│   ├── Prototipos/
│   ├── Requisitos_Funcionales/
│   ├── Requisitos_No_Funcionales/
│   ├── Evidencias/
│   ├── Historias_De_Usuario/
│   ├── Actas/
│   └── Plan_De_Trabajo/
│
├── app/
│   ├── Backend/
│   └── Frontend/
│
└── README.md
```

> **Stack:** Python 3.11 · Django 4.2 · Angular 19 · MySQL 8 · Windows · VS Code

---

## 📁 Estructura de la aplicación

```bash
app/
├── Backend/
│   ├── tienda_pachito/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── apps/
│   │   ├── productos/
│   │   ├── ventas/
│   │   ├── compras/
│   │   └── reportes/
│   │
│   ├── sql/
│   │   ├── 01_crear_base_datos.sql
│   │   └── 02_datos_iniciales.sql
│   │
│   ├── manage.py
│   └── requirements.txt
│
└── Frontend/
```

---

## 🗄️ PASO 1 — Crear la base de datos en MySQL Workbench

1. Abre MySQL Workbench y conéctate a tu servidor local
2. Abre el archivo: `Backend/sql/01_crear_base_datos.sql`
3. Ejecuta el script (⚡ o Ctrl + Shift + Enter)
4. Debes ver: `Base de datos tienda_pachito creada correctamente ✅`

---

## ⚙️ PASO 2 — Configurar credenciales en settings.py

```python
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'tienda_pachito',
        'USER':     'root',
        'PASSWORD': '1234',
        'HOST':     'localhost',
        'PORT':     '3306',
    }
}
```

---

## 🐍 PASO 3 — Configurar el Backend (Django)

```bash
cd tienda-pachito/Backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

> ✅ Backend disponible en: http://localhost:8000

### Verificación

* `http://localhost:8000/api/productos/`

  * `[]` → conexión exitosa
  * Error → revisar credenciales

---

## 📦 PASO 4 — Cargar datos iniciales (opcional)

Ejecutar en MySQL Workbench:

```
Backend/sql/02_datos_iniciales.sql
```

---

## 🅰️ PASO 5 — Configurar el Frontend (Angular)

```bash
cd tienda-pachito/Frontend

npm install
npm start
```

> ✅ Frontend disponible en: http://localhost:4200

---

## 🌐 Endpoints

| Método | Endpoint                                              | Descripción         |
| ------ | ----------------------------------------------------- | ------------------- |
| GET    | `/api/productos/`                                     | Listar productos    |
| POST   | `/api/productos/`                                     | Crear producto      |
| GET    | `/api/productos/{id}/`                                | Obtener producto    |
| PUT    | `/api/productos/{id}/`                                | Actualizar producto |
| DELETE | `/api/productos/{id}/`                                | Eliminar producto   |
| GET    | `/api/alertas/stock/`                                 | Stock bajo          |
| GET    | `/api/ventas/`                                        | Listar ventas       |
| GET    | `/api/ventas/?fecha=YYYY-MM-DD`                       | Ventas por fecha    |
| POST   | `/api/ventas/`                                        | Registrar venta     |
| GET    | `/api/compras/`                                       | Listar compras      |
| POST   | `/api/compras/`                                       | Registrar compra    |
| GET    | `/api/reportes/diario/?fecha=YYYY-MM-DD`              | Reporte diario      |
| GET    | `/api/reportes/rango/?fecha_inicio=...&fecha_fin=...` | Reporte por rango   |

---

## 📬 Ejemplos JSON

### Crear producto

```json
{
  "nombre": "Café 500g",
  "precio": 15000,
  "stock": 40,
  "stock_minimo": 10,
  "emoji": "☕"
}
```

### Actualizar producto

```json
{
  "precio": 3800,
  "stock_minimo": 20
}
```

### Registrar venta

```json
{
  "producto_id": 1,
  "cantidad": 3
}
```

### Registrar compra

```json
{
  "producto_id": 2,
  "cantidad": 50,
  "costo_unitario": 3200
}
```

---
## 🧪 Pruebas Postman

La colección de pruebas está en la carpeta `/postman`.

### Cómo importar en Postman:
1. Abre Postman
2. Clic en **Import**
3. Arrastra el archivo `Tienda_Pachito.postman_collection.json`
4. También importa el archivo de entorno `Tienda_Pachito.postman_environment.json`
5. Selecciona el entorno **Tienda Pachito - Local** en la esquina superior derecha
6. Asegúrate que Django esté corriendo antes de ejecutar las pruebas
---
## 🔧 Solución de Problemas

**Error 1045 (Access denied)**
→ Credenciales incorrectas en `settings.py`

**Error 2003 (Can't connect to MySQL)**
→ MySQL no está corriendo

**ModuleNotFoundError: MySQLdb**
→ Ejecutar:

```bash
pip install mysqlclient
```

**Error instalando mysqlclient en Windows**
→ Instalar Microsoft C++ Build Tools
→ Alternativa:

```bash
pip install mysqlclient --find-links https://www.lfd.uci.edu/~gohlke/pythonlibs/
```

---

## 📋 Backlog completado

| Historia | Descripción            | Estado |
| -------- | ---------------------- | ------ |
| PB-01    | Registro de Productos  | ✅      |
| PB-02    | Registro de Ventas     | ✅      |
| PB-03    | Actualización de Stock | ✅      |
| PB-04    | Registro de Compras    | ✅      |
| PB-05    | Reporte Diario         | ✅      |
| PB-06    | Alerta de Stock Bajo   | ✅      |
