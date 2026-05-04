# 🛒 Proyecto Tienda Pachito

Sistema de gestión para la administración de una tienda local, enfocado en mejorar el control de inventario, registro de ventas y generación de reportes.

---

## 📌 Descripción

Este proyecto tiene como objetivo desarrollar un sistema que permita gestionar de manera eficiente las operaciones principales de una tienda, reduciendo errores asociados al manejo manual de la información.

El sistema permite:

- 📦 Registro de productos  
- 💰 Registro de ventas  
- 📊 Control de inventario  
- 🏪 Registro de compras a proveedores  
- 📈 Generación de reportes de ventas  
- ⚠️ Alertas de stock bajo  

---

## 🎯 Objetivo del sistema

Optimizar la administración del negocio mediante la automatización de procesos clave, mejorando la precisión de los datos y facilitando la toma de decisiones.

---

## 🧠 Metodología de desarrollo

El proyecto se desarrolla utilizando la metodología ágil **Scrum**, organizando el trabajo mediante:

- 📋 Product Backlog  
- 👤 Historias de usuario  
- 🗺️ Mapa de historias de usuario (Story Map)  
- 📅 Daily Scrum (actas de reunión)  
- 📄 Requisitos funcionales  

---

## 👥 Equipo de trabajo

- **Product Owner:** Ángel Antonio Suárez Vera  
- **Scrum Master:** Manuel Alejandro Posada Zartha  
- **Development Team:**  
  - Wilson Alejandro Cespedes Alarcón  
  - David Felipe Lucero Trujillo  

---

## 🧩 Historias de Usuario

Las funcionalidades del sistema están definidas mediante las siguientes historias de usuario:

- **HU-01:** Registro de productos  
- **HU-02:** Registro de ventas  
- **HU-03:** Actualización automática de stock  
- **HU-04:** Registro de compras a proveedores  
- **HU-05:** Reporte diario de ventas  
- **HU-06:** Alerta de stock bajo  

---

## 🗂️ Estructura del repositorio

```bash
Proyecto-Tienda-Pachito
│
├── 1.Plan_De_Trabajo
├── 2.Actas
├── 3.Historias_De_Usuario
├── 4.Requisitos_Funcionales
├── 5.Requisitos_No_Funcionales
├── 6.Prototipos
├── 7.DiagramasUML
├── 8.Aplicación
└── 9.Evidencias

> **Stack:** Python 3.11 + Django 4.2 · Angular 19 · MySQL 8 · Windows · VS Code

---

## 📁 Estructura de la aplicacion

```
tienda-pachito/
├── Backend/
│   ├── tienda_pachito/
│   │   ├── settings.py          # ← Configura tus credenciales MySQL aquí
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── productos/           # Modelo + Views ORM (PB-01, PB-03, PB-06)
│   │   ├── ventas/              # Modelo + Views ORM (PB-02)
│   │   ├── compras/             # Modelo + Views ORM (PB-04)
│   │   └── reportes/            # Views ORM (PB-05)
│   ├── sql/
│   │   ├── 01_crear_base_datos.sql   # Ejecutar en MySQL Workbench primero
│   │   └── 02_datos_iniciales.sql    # Ejecutar después de migrate
│   ├── manage.py
│   └── requirements.txt
└── Frontend/  (sin cambios)
```

---

## 🗄️ PASO 1 — Crear la base de datos en MySQL Workbench

1. Abre **MySQL Workbench** y conéctate a tu servidor local
2. Abre el archivo `Backend/sql/01_crear_base_datos.sql`
3. Ejecuta el script (⚡ o Ctrl+Shift+Enter)
4. Deberías ver: `Base de datos tienda_pachito creada correctamente ✅`

---

## ⚙️ PASO 2 — Configurar credenciales en settings.py

Abre `Backend/tienda_pachito/settings.py` y edita esta sección:

```python
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'tienda_pachito',   # nombre de la BD (no cambiar)
        'USER':     'root',              # ← tu usuario MySQL
        'PASSWORD': '1234',              # ← tu contraseña MySQL
        'HOST':     'localhost',
        'PORT':     '3306',
    }
}
```

---

## 🐍 PASO 3 — Configurar el Backend (Django)

```bash
# Navegar a la carpeta Backend
cd tienda-pachito\Backend

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar dependencias (incluye mysqlclient)
pip install -r requirements.txt

# Crear las tablas en MySQL
python manage.py migrate

# Levantar el servidor
python manage.py runserver
```

> ✅ El backend estará en: **http://localhost:8000**

### Verificar que conectó bien:
Abre en el navegador: http://localhost:8000/api/productos/
- Si ves `[]` → conexión exitosa (sin datos aún)
- Si ves error → revisa usuario/contraseña en settings.py

---

## 📦 PASO 4 — Cargar datos iniciales (opcional)

Una vez que el servidor corra correctamente, ejecuta en MySQL Workbench:

`Backend/sql/02_datos_iniciales.sql`

Esto carga 6 productos, ventas y compras de ejemplo.

---

## 🅰️ PASO 5 — Configurar el Frontend (Angular)

```bash
# Segunda terminal
cd tienda-pachito\Frontend

# Instalar dependencias
npm install

# Levantar Angular
npm start
```

> ✅ El frontend estará en: **http://localhost:4200**

---

## 🌐 Endpoints Postman

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/productos/` | Listar todos los productos |
| POST | `/api/productos/` | Crear producto |
| GET | `/api/productos/{id}/` | Ver producto por ID |
| PUT | `/api/productos/{id}/` | Editar producto |
| DELETE | `/api/productos/{id}/` | Eliminar producto |
| GET | `/api/alertas/stock/` | Productos con stock bajo |
| GET | `/api/ventas/` | Listar ventas |
| GET | `/api/ventas/?fecha=YYYY-MM-DD` | Ventas por fecha |
| POST | `/api/ventas/` | Registrar venta |
| GET | `/api/compras/` | Listar compras |
| POST | `/api/compras/` | Registrar compra |
| GET | `/api/reportes/diario/?fecha=YYYY-MM-DD` | Reporte diario |
| GET | `/api/reportes/rango/?fecha_inicio=...&fecha_fin=...` | Reporte por rango |

### Ejemplos de cuerpo JSON para Postman:

**POST /api/productos/**
```json
{
  "nombre": "Café 500g",
  "precio": 15000,
  "stock": 40,
  "stock_minimo": 10,
  "emoji": "☕"
}
```

**PUT /api/productos/1/**
```json
{
  "precio": 3800,
  "stock_minimo": 20
}
```

**POST /api/ventas/**
```json
{
  "producto_id": 1,
  "cantidad": 3
}
```

**POST /api/compras/**
```json
{
  "producto_id": 2,
  "cantidad": 50,
  "costo_unitario": 3200
}
```

---

## 🔧 Solución de Problemas

### ❌ `django.db.utils.OperationalError: (1045) Access denied`
→ Usuario o contraseña incorrectos en `settings.py`

### ❌ `django.db.utils.OperationalError: (2003) Can't connect to MySQL`
→ MySQL no está corriendo. Inicia el servicio MySQL desde Windows Services o MySQL Workbench

### ❌ `ModuleNotFoundError: No module named 'MySQLdb'`
→ Ejecuta: `pip install mysqlclient`

### ❌ `mysqlclient` falla al instalar en Windows
→ Instala primero: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
→ O usa el wheel precompilado: `pip install mysqlclient --find-links https://www.lfd.uci.edu/~gohlke/pythonlibs/`

---

## 📋 Backlog completado

| Historia | Descripción | Estado |
|----------|-------------|--------|
| PB-01 | Registro de Productos | ✅ |
| PB-02 | Registro de Ventas | ✅ |
| PB-03 | Actualización de Stock (MySQL) | ✅ |
| PB-04 | Registro de Compras | ✅ |
| PB-05 | Reporte Diario | ✅ |
| PB-06 | Alerta de Stock Bajo | ✅ |

