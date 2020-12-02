FROM python:3.7-alpine
# dependencias
RUN apk add build-base jpeg-dev zlib-dev
# agregar los archivos locales al contenedor
ADD ./src /code
# cambiar el directorio
WORKDIR /code

RUN pip install -r dependences.txt

CMD ["python", "WebService.py"]