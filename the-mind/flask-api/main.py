import time

from flask import Flask, render_template, request
# pyre-ignore
from flask_socketio import SocketIO, join_room, leave_room, emit, send

from model.juego import Juego
from model.lobby import Lobby
from model.mind_control import MindControl

app = Flask("__main__")
socketio = SocketIO(app,
	engineio_logger=True,
	cors_allowed_origins=[
		'http://localhost:3000',
		'https://jonseijo.com',
		'https://www.jonseijo.com'],
	async_mode="gevent"
)

ROOMS = {}
themind = MindControl()

player_name_conexiones = {}
lobby_name_conexiones = {}


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
def on_connectar(param):
	emit('conectar_response', {'status': 'OK'})

@socketio.on('connect')
def on_connect():
	print("~~~~~~~~~~~~~~~~CONECTE THE MIND")
	emit('conectar_response', {'status': 'OK'})


@socketio.on('disconnect')
def on_disconnect():
	player_name = player_name_conexiones.pop(request.sid, None)
	lobby_name = lobby_name_conexiones.pop(request.sid, None)
	print('--DESCONECTO: ' + str(player_name))

	lobby_state = themind.desconectar_jugador(player_name)

	leave_room(lobby_name)
	socketio.emit('juego_terminado', lobby_state, room=lobby_name)
	socketio.emit('lobby_update', lobby_state, room=lobby_name)


@socketio.on('lobby_agregar_jugador')
def on_lobby_agregar_jugador(params):
	try:
		player_name = params['player_name']
		lobby_name = params['lobby_name']
		join_room(lobby_name)

		themind.agregar_jugador(player_name, lobby_name)

		# TODO: Ver que pasa cuando esta conexion ya existe.
		# Cuando desarrollo local se crean varias?
		player_name_conexiones[request.sid] = player_name
		lobby_name_conexiones[request.sid] = lobby_name

		socketio.emit('lobby_update', themind.estado_lobby(lobby_name), room=lobby_name)

	except Exception as ex:
		emit('lobby_update', {'error': str(ex)}, room=lobby_name)


@socketio.on('juego_iniciar')
def on_juego_iniciar():
	lobby_name = lobby_name_conexiones[request.sid]
	themind.iniciar_juego_en(lobby_name)
	socketio.emit('juego_iniciado', room=lobby_name)


@socketio.on('poner_carta')
def on_poner_carta(params):
	player_name = player_name_conexiones.get(request.sid, None)
	lobby_name = lobby_name_conexiones.get(request.sid, None)
	if not player_name or not lobby_name:
		return

	carta = int(params['carta'])

	themind.colocar_carta(lobby_name, player_name, carta)
	socketio.emit('juego_update', themind.estado_juego(lobby_name), room=lobby_name)


@socketio.on('subir_nivel')
def on_subir_nivel():
	lobby_name = lobby_name_conexiones[request.sid]
	themind.subir_nivel_en(lobby_name)
	socketio.emit('juego_update', themind.estado_juego(lobby_name), room=lobby_name)


@socketio.on('juego_quiero_terminar')
def on_juego_quiero_terminar():
	lobby_name = lobby_name_conexiones[request.sid]
	themind.terminar_juego(lobby_name)
	socketio.emit('juego_terminado', themind.estado_lobby(lobby_name), room=lobby_name)


@socketio.on('lobby_estado')
def on_lobby_estado():
	lobby_name = lobby_name_conexiones[request.sid]
	emit('lobby_update', themind.estado_lobby(lobby_name))


@socketio.on('juego_estado')
def on_juego_estado():
	lobby_name = lobby_name_conexiones[request.sid]
	emit('juego_update', themind.estado_juego(lobby_name))


if __name__ == "__main__":
	socketio.run(app, host='127.0.0.1', port=5000, debug=True)
