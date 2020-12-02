FROM python:3.7-alpine
# dependenciass
RUN apk add build-base jpeg-dev zlib-dev
# agregar los archivos locales al contenedor
ADD ./src /code
# cambiar el directorio
WORKDIR /code
# corre el pip3 con las dependencias
RUN pip3 install -r dependences.txt

CMD ["python", "WebService.py"] 