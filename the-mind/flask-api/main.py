import time

from flask import Flask, render_template, request
# pyre-ignore
from flask_socketio import SocketIO, join_room, emit, send

from model.juego import Juego
from model.lobby import Lobby

app = Flask("__main__")
socketio = SocketIO(app)
ROOMS = {}

info_conexiones = {}

@app.route("/")
def my_index():
	return "Mejor proba con localhost:3000"


@app.route("/time")
def time_api():
	return {'time': time.time()}


# DEBUG
@app.route("/reset")
def reset_debug():
	themind.lobby.reset()
	return "reset"


@socketio.on('conectar')
def on_connect(param):
	print("Alguien se conecto!")
	emit('conectar_response', {'status': 'OK'})


@socketio.on('disconnect')
def on_disconnect():
	name = info_conexiones.pop(request.sid, None)
	print('--DESCONECTO: ' + str(name))

	themind.juego.terminar()
	themind.lobby.remover_jugador(name)

	socketio.emit('juego_terminado', themind.lobby.estado())
	socketio.emit('lobby_update', themind.lobby.estado())


@socketio.on('lobby_agregar_jugador')
def on_lobby_agregar_jugador(params):
	try:
		name = params['name']
		themind.lobby.agregar_jugador(name)

		info_conexiones[request.sid] = name

		socketio.emit('lobby_update', themind.lobby.estado())

	except Exception as ex:
		emit('lobby_update', {'error': str(ex)})


@socketio.on('juego_iniciar')
def on_juego_iniciar():
	if len(themind.lobby.jugadores()) >= 2:
		themind.juego = Juego.iniciar(jugadores=themind.lobby.jugadores())
		socketio.emit('juego_iniciado')


@socketio.on('poner_carta')
def on_poner_carta(params):
	name = info_conexiones.get(request.sid, None)
	if not name:
		return

	carta = int(params['carta'])
	themind.juego.poner_carta(name, carta)
	socketio.emit('juego_update', themind.juego.estado())


@socketio.on('subir_nivel')
def on_subir_nivel():
	# TODO: try catch aca
	themind.juego.subir_nivel()
	socketio.emit('juego_update', themind.juego.estado())


@socketio.on('juego_quiero_terminar')
def on_juego_quiero_terminar():
	themind.juego.terminar()
	socketio.emit('juego_terminado', themind.lobby.estado())


@socketio.on('lobby_estado')
def on_lobby_estado():
	emit('lobby_update', themind.lobby.estado())


@socketio.on('juego_estado')
def on_juego_estado():
	emit('juego_update', themind.juego.estado())


class TheMindApi():
	def __init__(self) -> None:
		self.juego = None
		self.lobby = Lobby()


if __name__ == "__main__":
# def app():
	themind = TheMindApi()
	socketio.run(app, host='0.0.0.0', port=5000, debug=True)
