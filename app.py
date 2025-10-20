#Fernando Mejia Lechuga
#Bahena Praxedis Maria Adalid
#Estrada Romero Angeles
#Emiliano
#Jesus
#Josh

#Importacion y conf basica
from flask import Flask, render_template, request, session
import random

#Creación de la Aplicación Flask y definición de una llave secreta 
app = Flask(__name__)
app.secret_key = 'clave_secreta'

#genera número aleatorio del 1-100
def nuevo_numero():
    return random.randint(1, 100)
                          
#Página principal del juego
@app.route('/')
def index():
    if 'numero' not in session:
        iniciar_juego()
    return render_template('index.html', puntos=session['puntos'], intentos=session['intentos'])

#función /adivinar
#Configuración inicial y validación
@app.route('/adivinar', methods=['POST'])
def adivinar():
    if 'numero' not in session:
        iniciar_juego()

#Obtención de datos del jugador
    numero_secreto = session['numero']
    intento = int(request.form['numero'])
    session['intentos'] += 1
    mensaje = ''
    mensaje_distancia = ''


#Obtención de datos del jugador
    numero_secreto = session['numero']
    intento = int(request.form['numero'])
    session['intentos'] += 1

    mensaje = ''
    mensaje_distancia = ''

# Verificar si acertó o no
if intento == numero_secreto:
    session['puntos'] += 100
    mensaje = f'¡Correcto! El número era {numero_secreto}.'
    session['numero'] = nuevo_numero()
elif intento < numero_secreto:
    mensaje = 'El número es mayor.'
else:
    mensaje = 'El número es menor.'

    # Calcular qué tan cerca estuvo
diff = abs(numero_secreto - intento)
if diff <= 9:
    mensaje_distancia = 'Muy cerca.'
elif diff <= 19:
    mensaje_distancia = 'Cerca.'
elif diff <= 39:
    mensaje_distancia = 'Lejos.'
else:
    mensaje_distancia = 'Muy lejos.'

# Unir mensaje principal y distancia
if intento == numero_secreto:
    session['puntos'] += 100
    mensaje = f'¡Correcto! El número era {numero_secreto}.'
    session['numero'] = nuevo_numero()
else:
    if intento < numero_secreto:
        pista = 'El número es mayor.'
    else:
        pista = 'El número es menor.'

    diff = abs(numero_secreto - intento)
    if diff <= 9:
        distancia = 'Muy cerca.'
    elif diff <= 19:
        distancia = 'Cerca.'
    elif diff <= 39:
        distancia = 'Lejos.'
    else:
        distancia = 'Muy lejos.'

    mensaje = f'{pista} {distancia}'

# Limpieza de condiciones para simplificar código
if diff <= 9:
    distancia = 'Muy cerca.'
elif diff <= 19:
    distancia = 'Cerca.'
elif diff <= 39:
    distancia = 'Lejos.'
else:
    distancia = 'Muy lejos.'

# En tu ruta Flask
return render_template('index.html', mensaje=mensaje)

#Mostrar el resultado al jugador
return render_template('index.html',
                       mensaje=f"{mensaje} {mensaje_distancia}",
                       puntos=session['puntos'],
                       intentos=session['intentos'])

                       #Reiniciar el juego y ejecutar el servidor
                       @app.route('/reiniciar')
                       def reiniciar():