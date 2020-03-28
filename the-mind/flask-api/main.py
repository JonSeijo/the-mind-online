import time

from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

from model.juego import Juego

app = Flask("__main__")
socketio = SocketIO(app, cors_allowed_origins='http://localhost:3000')
ROOMS = {}

@app.route("/")
def my_index():
	return "Mejor proba con localhost:3000"

@app.route("/time")
def time_api():
	return {'time': time.time()}

@socketio.on('connectar')
def on_connect(param):
	print("param: ", param)
	emit('connect_response', param)

if __name__ == "__main__":

	socketio.run(app, port=5000, debug=True)

