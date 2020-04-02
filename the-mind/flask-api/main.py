import time

from flask import Flask, render_template, request
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

# DEBUG
@app.route("/reset")
def reset_debug():
	lobby.reset()
	return "reset"

@socketio.on('conectar')
def on_connect(param):
	print("Alguien se conecto!")
	emit('conectar_response', {'status': 'OK'})

@socketio.on('disconnect')
def on_disconnect():
	name = info_conexiones.pop(request.sid, None)
	print('--DESCONECTO: ' + str(name))

	lobby.remover_jugador(name)
	socketio.emit('lobby_update', lobby.estado())


@socketio.on('lobby_agregar_jugador')
def on_lobby_agregar_jugador(params):
	try:
		name = params['name']
		lobby.agregar_jugador(name)

		info_conexiones[request.sid] = name

		socketio.emit('lobby_update', lobby.estado())

	except Exception as ex:
		emit('lobby_update', {'error': str(ex)})

@socketio.on('juego_iniciar')
def on_juego_iniciar():
	if len(lobby.jugadores()) >= 2:
		juego = Juego()
		socketio.emit('juego_iniciado')


if __name__ == "__main__":
	info_conexiones = {}
	lobby = Lobby()
	juego = None
	socketio.run(app, port=5000, debug=True)

