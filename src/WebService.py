#!/bin/python3

from flask import Flask, request, Response
import requests, json, urllib.parse
from bs4 import BeautifulSoup
from markupsafe import escape
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, CDK classroom!'

@app.route('/saludo/<persona>')
def saludoDinamico(persona):
    return 'Hola %s, bienvenido!!' % persona

@app.route('/cuadrado/<float:num>')
def calculaCuadrado(num):
    resp = num * num
    return 'Respuesta: %f' % resp

@app.route('/curso', methods=['POST', 'GET'])
def webScrap():
    data = {}    
    if request.method == 'POST':
        try: 
            data = request.get_json()
            busqueda = data['busqueda']            
            data['cursos'] = []
            busquedaText = busqueda.lower()
            busqueda = urllib.parse.quote(busqueda)
            page = requests.get('https://www.tecgurus.net/cursos?busqueda=' + busqueda)

            # Create a BeautifulSoup object
            soup = BeautifulSoup(page.text, 'html.parser')
            cursos_list = soup.find(class_='right-service-box')
            # Pull text from all instances of <a> tag within BodyText div
            cursos_items = cursos_list.find_all('img')
            for curso in cursos_items:
                tituloCurso = curso.get('alt')
                if tituloCurso.lower().find(busquedaText) != -1:
                    data['cursos'].append({'nombre': curso.get('alt')}) 
        except:
            data['error'] = "Método no aceptado"
    else:
        data['error'] = "Método no aceptado"
    return json.dumps(data);

@app.route('/audiosaludo/<msgText>')
def audiotext(msgText):
	saludohtml = "<audio controls autoplay> <source src='https://code.responsivevoice.org/getvoice.php?text=%s&lang=es-MX&engine=g1&name=&pitch=0.5&rate=0.5&volume=1&key=uu8DEkxz&gender=female' type='audio/mpeg'> </audio>" % msgText	
	return saludohtml

@app.route('/convertir', methods=['POST', 'GET'])
def cambio_base():
    data = request.get_json()
    decimal = int(data['decimal'])
    base = int(data['base'])
    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        decimal = decimal // base
    return str(decimal) + conversion

#### Procedimiento para graficar ####
@app.route('/grafica.png', methods=['POST', 'GET'])
def plot_png():
   if request.method == 'POST':
      data = request.get_json()
      print(data)
      if data['tipo'] == 'pie':
         fig = pie(data)
      elif data['tipo'] == 'bar':
         fig = bar(data)
      else:
         fig = line(data)
      output = io.BytesIO()
      FigureCanvas(fig).print_png(output)
      return Response(output.getvalue(), mimetype='image/png')
   else:
      return "Petición GET no es válida"

def bar(datos):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    #data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
    #names = list(data.keys())
    #values = list(data.values())
    axis.bar(datos['nombres'], datos['valores'])
    return fig

def pie(datos):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.pie(datos['valores'], labels=datos['nombres'], autopct='%1.1f%%',
         shadow=True, startangle=90)
    axis.axis('equal')
    return fig

def line(datos):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(datos['nombres'], datos['valores'])
    return fig

###########

@app.route('/evidencia', methods=['POST', 'GET'])
def consumo():    
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        imagen = Image.open('./comida.jpg')
        imagen.show()
        return "<b>Se mando: título </b> %s" %data['titulo'] + ", <b> descripción: </b> %s " %data['descripcion']  + "  <b> calorías: </b> %i" %data['caloria'] + " <b> fecha: </b> %s" %data['fecha']
    else:
        return "Not found method"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
