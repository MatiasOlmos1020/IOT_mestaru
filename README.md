# Cultivo API

Este proyecto es una API REST creada en Python utilizando Flask, diseñada para recibir y procesar datos enviados desde un ESP32. Es parte de un proyecto de aprendizaje que se desarrollará progresivamente hasta incluir funcionalidades avanzadas como almacenamiento en bases de datos y despliegue en Docker.

## Requisitos

Asegúrate de tener instalados los siguientes programas:

- **Python 3.12.6**
- **pip** (Administrador de paquetes de Python, incluido con Python 3.12.6)
- Opcional: **Git** para clonar el repositorio

## Configuración inicial

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd cultivo_api
   ```

2. Crea y activa un entorno virtual para el proyecto:

   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

## Estructura del proyecto

```plaintext
cultivo_api/
├── src/
│   ├── api/
│   │   ├── app.py             # Archivo principal para levantar el servidor
│   │   ├── routes/
│   │   │   └── sensor_routes.py  # Rutas para manejar los datos de sensores
│   ├── requirements.txt       # Lista de dependencias del proyecto
├── README.md                  # Documentación del proyecto
```

## Cómo ejecutar el servidor

1. Asegúrate de que tu entorno virtual esté activado:

   ```bash
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

2. Dirígete a la carpeta `src/api` y ejecuta el servidor:

   ```bash
   cd src/api
   python app.py
   ```

3. Si todo está configurado correctamente, el servidor estará disponible en `http://127.0.0.1:5000`.

## Pruebas de las rutas

Puedes probar las rutas de la API utilizando herramientas como [Postman](https://www.postman.com/) o `curl` desde la línea de comandos. Por ejemplo:

### Ruta `/api/data` (POST)

```bash
curl -X POST http://127.0.0.1:5000/api/data \
    -H "Content-Type: application/json" \
    -d '{"temperature": 25, "humidity": 60}'
```

Respuesta esperada:

```json
{
    "message": "Datos recibidos correctamente"
}
```

## Notas importantes

- Este proyecto aún no está preparado para Docker, pero la configuración actual facilita su futura dockerización.
- A medida que avancemos, se añadirá una base de datos para almacenar los datos enviados por el ESP32.

---

Si tienes preguntas o problemas, ¡no dudes en abrir un issue en este repositorio! 😊
