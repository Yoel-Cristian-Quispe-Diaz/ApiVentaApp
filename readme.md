# 🛒 Tienda Virtual API

Una API RESTful robusta y moderna desarrollada con **FastAPI**, **SQLAlchemy** y **Pydantic** para la gestión integral de una tienda en línea (usuarios, categorías, productos, ventas y detalles de venta).

---

## 🚀 Tecnologías Utilizadas

- **Lenguaje:** Python 3.11+
- **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
- **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Validación de Datos:** [Pydantic v2](https://docs.pydantic.dev/)
- **Base de Datos:** PostgreSQL (compatible con MySQL / MariaDB vía controladores incluidos)

---

## 📁 Estructura del Proyecto

```text
├── crud.py            # Operaciones de base de datos (Create, Read, Update, Delete)
├── database.py        # Configuración de conexión y sesión a la base de datos
├── main.py            # Instancia de FastAPI, configuración de rutas y endpoints
├── models.py          # Modelos de tablas ORM (SQLAlchemy)
├── schemas.py         # Esquemas de validación y serialización (Pydantic)
├── requirements.txt   # Dependencias del proyecto
├── runtime.txt        # Versión de Python especificada (3.11.9)
├── Procfile           # Comando de ejecución para despliegues (Heroku / Render)
└── .env               # Variables de entorno (no incluir en repositorios públicos)
```

---

## ⚙️ Requisitos Previos

- Python 3.11 o superior instalado.
- Servidor de base de datos PostgreSQL (o MySQL) en ejecución.
- Gestor de paquetes `pip` y entorno virtual `venv`.

---

## 🛠️ Instalación y Configuración Local

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>
```

### 2. Crear y activar entorno virtual

- En **Linux / macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- En **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto y define la cadena de conexión a la base de datos:

```dotenv
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/tienda
```

> **Nota:** Si usas MySQL, el formato de conexión sería:
> `DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/tienda`

---

## ▶️ Ejecución del Servidor

Inicia el servidor local de desarrollo con recarga automática:

```bash
uvicorn main:app --reload
```

El servidor estará disponible por defecto en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📖 Documentación Interactiva de la API

Una vez iniciado el servidor, accede a la documentación interactiva provista automáticamente por FastAPI:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Resumen de Endpoints

### 👤 Usuarios (`/usuarios`)
| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/usuarios/` | Crear un nuevo usuario |
| `GET` | `/usuarios/` | Listar usuarios (con paginación `skip` y `limit`) |
| `GET` | `/usuarios/{id_usuario}` | Obtener un usuario por ID |
| `PUT` | `/usuarios/{id_usuario}` | Actualizar un usuario existente |
| `DELETE` | `/usuarios/{id_usuario}` | Eliminar un usuario |

### 🏷️ Categorías (`/categorias`)
| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/categorias/` | Registrar una nueva categoría |
| `GET` | `/categorias/` | Listar categorías |
| `GET` | `/categorias/{id_categoria}` | Obtener categoría por ID |
| `PUT` | `/categorias/{id_categoria}` | Actualizar una categoría |
| `DELETE` | `/categorias/{id_categoria}` | Eliminar una categoría |

### 📦 Productos (`/productos`)
| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/productos/` | Registrar un nuevo producto |
| `GET` | `/productos/` | Listar productos |
| `GET` | `/productos/{id_producto}` | Obtener producto por ID |
| `PUT` | `/productos/{id_producto}` | Actualizar un producto |
| `DELETE` | `/productos/{id_producto}` | Eliminar un producto |

### 💳 Ventas (`/ventas`)
| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/ventas/` | Crear una orden de venta |
| `GET` | `/ventas/` | Listar ventas registradas |
| `GET` | `/ventas/{id_venta}` | Obtener venta por ID |
| `PUT` | `/ventas/{id_venta}` | Actualizar datos de una venta |
| `DELETE` | `/ventas/{id_venta}` | Eliminar registro de venta |

### 📋 Detalle de Venta (`/detalle_venta`)
| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/detalle_venta/` | Asociar un ítem/producto a una venta |
| `GET` | `/detalle_venta/` | Listar detalles de ventas |
| `GET` | `/detalle_venta/{id_detalle}` | Obtener detalle específico por ID |
| `PUT` | `/detalle_venta/{id_detalle}` | Actualizar detalle de venta |
| `DELETE` | `/detalle_venta/{id_detalle}` | Eliminar un detalle de venta |

---

## ☁️ Despliegue (PaaS)

El repositorio incluye soporte para plataformas como **Render**, **Railway** o **Heroku**:

- **Comando de inicio (`Procfile`):**
  ```text
  web: uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- **Versión de runtime:** Definida en `runtime.txt` como `python-3.11.9`.
- Recuerda configurar la variable de entorno `DATABASE_URL` en el panel de control de tu proveedor de hosting.