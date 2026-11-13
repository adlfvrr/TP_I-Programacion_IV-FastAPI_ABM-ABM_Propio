# TP I - Programación IV: FastAPI ABM (Backend)

Repositorio correspondiente al Trabajo Práctico de la materia **Programación IV**, implementando una API REST con operaciones ABM (Alta, Baja, Modificación y consulta / CRUD) utilizando **FastAPI**, validación de datos con **Pydantic** y ejecución mediante **Uvicorn**.

Dentro del Trabajo práctico, se completó lo pedido del abm de la carpeta **clase-fastapi**, así como se creó un abm con una entidad propia a elección. En este caso,
se eligió la entidad de **Films**, películas donde se puedan listar y filtrar por rating, crear, actualizar y borrar.
Las películas están compuestas de:
- id
- name 
- year 
- rating 
- studio

---

## 🛠️ Prerrequisitos

* **Python** (versión 3.10 o superior recomendada) instalado en tu sistema.
* Gestor de paquetes `pip`.

---

## 🚀 Guía de Instalación y Configuración

### 1. Clonar el repositorio
Abre tu terminal y clona el proyecto (o descárgalo y descomprímelo):

```bash
git clone https://github.com/adlfvrr/TP_I-Programacion_IV-FastAPI_ABM-ABM_Propio.git
cd TP_I-Programacion_IV-FastAPI_ABM-ABM_Propio
```
Elegimos uno de los dos proyectos dentro, ya sea clase-fastapi, como abm-entidad-propia
```bash
cd clase-fastapi
--
cd abm-entidad-propia
```

### 2. Crear el entorno virtual
Es una buena práctica aislar las dependencias del proyecto en un entorno virtual. Ejecuta el siguiente comando en la raíz del proyecto:

* **En Windows (CMD / PowerShell):**
  ```bash
  python -m venv .venv
  ```
* **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  ```

### 3. Activar el entorno virtual
Activa el entorno virtual antes de instalar las dependencias:

* **En Windows (CMD):**
  ```bash
  venv\Scripts\activate.bat
  ```
* **En Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **En Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instalar las dependencias
Una vez activo el entorno virtual (verás `(venv)` al inicio de tu línea de comandos), instala los paquetes requeridos:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Ejecución de la Aplicación

Dado que el archivo principal `main.py` se encuentra en la raíz del proyecto, puedes levantar el servidor de desarrollo local con recarga automática ejecutando:

```bash
uvicorn main:app --reload
```

El servidor se iniciará por defecto en `http://127.0.0.1:8000`.

---

## 📖 Documentación de la API (Swagger UI)

Una vez que la aplicación esté corriendo, puedes acceder a la documentación interactiva generada automáticamente por FastAPI para probar los endpoints del ABM:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc (Alternativa):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints disponibles -ABM FILMS- (ver Swagger para detalles)
- GET - /films/{ rating } - Query param vacío devuelve todas las películas. Se ingresa un rating (0-10), se filtran por el mismo -
- POST - /films - Creación de película, respetando el rango de rating (0-10) y año (1970-2026) de las películas -
- PUT - /films/{id}?{query's params} - Actualización de datos de películas, pasando datos como nombre, rating, año y estudio como query params -
- DELETE - /films/{id} - Borrado de película por id 