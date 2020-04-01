import time

from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

from model.juego import Juego
from model.lobby import Lobby

app = Flask("__main__")
socketio = SocketIO(app, cors_allowed_origins='http://localhost:3000')
ROOMS = {}

@app.route("/")
def my_index():
	return "Mejor proba con localhost:3000"

@app.route("/time")
def time_api():
	return {'time': time.time()}

@socketio.on('conectar')
def on_connect(param):
	print("Alguien se conecto!")
	emit('conectar_response', {'status': 'OK'})

@socketio.on('agregar_jugador_lobby')
def on_agregar_jugador_lobby(params):
	try:
		lobby.agregar_jugador(params['name'])
		socketio.emit('lobby_update', lobby.estado())

	except Exception as ex:
		emit('lobby_update', {'error': str(ex)})

if __name__ == "__main__":
	lobby = Lobby()
	socketio.run(app, port=5000, debug=True)

