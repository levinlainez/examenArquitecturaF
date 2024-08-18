# Usa una imagen oficial de Python como base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos y el código fuente al contenedor
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "/examen_binaria/manage.py", "runserver", "0.0.0.0:8000"]
