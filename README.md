# ¡Hola neurona! - Streamlit App

Esta aplicación permite simular una neurona artificial con una, dos o tres entradas y sesgo, visualizando el resultado de la suma ponderada. Incluye una interfaz gráfica sencilla y moderna usando Streamlit.

## Estructura del proyecto
- `app.py`: Código principal de la aplicación.
- `requirements.txt`: Dependencias de Python.
- `Dockerfile` y `docker-compose.yml`: Para ejecución y despliegue con Docker.
- `img/neurona.png`: Imagen decorativa de la neurona.

## Uso local
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta la app:
   ```bash
   streamlit run app.py
   ```

## Uso con Docker
1. Construye y ejecuta el contenedor:
   ```bash
   docker-compose up --build
   ```
2. Accede a la app en [http://localhost:8501](http://localhost:8501)
## Link de la app
https://ejercicio-app-neurona-bftqgtad2nxpz7zgzh2bot.streamlit.app
## Autor
© Ismael Guerrero Martín
