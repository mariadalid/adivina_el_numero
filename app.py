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