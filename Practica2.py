import ISS_Info #Libreria de la estacion espacial
import turtle #Libreria para la ventana y grafica
import time
import threading #Libreria para ejecutar el proceso

screen = turtle.Screen() #Creamos la ventana emergente
screen.title("ISS TRACKER") #Titulo de la ventana
screen.setup(720, 360) #Indicamos el tamanio de la ventana dependiendo de la imagen que utilicemos
screen.colormode(255) #habilitamos para utilizar configuracion RGB
screen.setworldcoordinates(-180,-90,180,90) #indicamos las coordenadas maximas y minimas de latitud y longitud
screen.bgpic("world.png") #ponemos la imagen de mapamundi como fondo de la ventana
screen.register_shape("iss.gif") #indicamos el icono que representara al satelite


iss = turtle.Turtle() #creamos el icono de satelite
iss.shape("iss.gif") #ponemos la imagen del satelite como el icono
iss.penup()

def tracker():
    while True:
        try:
            location = ISS_Info.iss_current_loc() #pedimos los datos de la estacion espacial
            lat = location['iss_position']['latitude'] # extraemos la latitud de la cadena de datos que recibimos
            lon = location['iss_position']['longitude'] #extraemos la longitud de la cadena de datos
            screen.title("ISS TRACKER: (Latitude: {}, Longitude: {})".format(lat,lon)) #modificamos el titulo agregando latitud y longitud
            iss.goto(float(lon),float(lat)) #movemos el icono a las coordenadas correspondientes
            iss.dot(2, 255, 0, 0) #dejamos trazado el recorrido del satelite
            time.sleep(5) #repetimos cada 5 segundos
        except Exception as e:
            print(str(e))
            break
        
t = threading.Thread(target=tracker())
t.start()