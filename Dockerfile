# descarga y crea la versión más actualizada de alpine
FROM alpine:latest

#instala en alpine linux la versión de python(con 'python-dev'
# contine pip) y actualiza pip
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

#crea directorio
WORKDIR /app 

#copia el contenido al directorio creado
COPY . /app 

#instala los paquetes necesarios
RUN pip3 install --no-cache-dir -r requirements.txt

#corre la aplicacion
CMD ["python3","./app.py"]