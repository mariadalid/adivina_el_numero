#Bahena Praxedis Maria Adalid
#Estrada Romero Angeles
#Dario Emiliano 
#Alexis Joshua Beltran Santiago


print("¡Bienvenido al juego de Adivina el Número!")

#Reiniciar juego y ejecutar servidor
@app.route('/reiniciar')
def reiniciar():
    iniciar_juego()
    return render_template('index.html', puntos=session['puntos'], intentos=session['intentos'])

if __name__ == '__main__':
    app.run(debug=True)
