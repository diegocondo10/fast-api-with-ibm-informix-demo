# Usar la imagen oficial de Python 3.11
FROM python:3.11-slim-buster

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos del proyecto al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar FastAPI con hot reload
CMD ["uvicorn", "app.main:main_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
