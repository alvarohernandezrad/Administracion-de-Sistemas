# Imagen base
FROM python:3.7-alpine

# Ubicarse dentro de un directorio como directorio de trabajo
WORKDIR /code

# Descargar e instalar dependencias
RUN apk add --no-cache gcc musl-dev linux-headers
 
# Copiar un determinado archivo en un directorio
COPY ./requirements.txt /code

# Ejecutar el comando para instalar dependecias
RUN pip install -r requirements.txt

# Copia el fichero app.py dentro de /code
COPY ./actualizar_precios.py /code

# Comando de arranque
CMD ["python3", "actualizar_precios.py"]
