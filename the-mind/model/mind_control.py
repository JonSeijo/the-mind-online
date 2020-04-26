# pyre-strict

from typing import Any, Dict, List, Set

from model.exceptions import *
from model.lobby import Lobby
from model.juego import Juego


class MindControl():

	def __init__(self) -> None:
		self._lobby_de : Dict[str, Lobby] = {}
		self._lobbies_por_lid : Dict[str, Lobby] = {}
		self._juego_por_lid : Dict[str, Lobby] = {}

	def agregar_lobby(self, lobby_id: str) -> Lobby:
		if lobby_id in self._lobbies_por_lid:
			raise LobbyExistenteException

		lobby = Lobby()
		self._lobbies_por_lid[lobby_id] = lobby
		return lobby

	def agregar_jugador(self, jugador: str, lobby_id: str) -> None:
		if jugador in self._jugadores():
			raise JugadorExistenteException()

		if lobby_id not in self._lobbies():
			raise LobbyInexistenteException()

		lobby = self._lobbies_por_lid[lobby_id]
		self._lobby_de[jugador] = lobby
		lobby.agregar_jugador(jugador)

	def iniciar_juego_en(self, lobby_id: str) -> None:
		if lobby_id not in self._lobbies():
			raise LobbyInexistenteException()

		lobby = self._lobbies_por_lid[lobby_id]

		if len(lobby.jugadores()) < 2:
			raise LobbyIncompletoException()

		if lobby_id in self._juego_por_lid:
			juego = self._juego_por_lid[lobby_id]
			if not juego.terminado():
				raise JuegoEnCursoException()

		juego = Juego.iniciar(jugadores=lobby.jugadores())
		self._juego_por_lid[lobby_id] = juego


	def estado_lobby(self, lobby_id: str) -> Dict[str, Any]:
		if lobby_id not in self._lobbies():
			raise LobbyInexistenteException()

		return self._lobbies_por_lid[lobby_id].estado()

	def estado_juego(self, lobby_id: str) -> Dict[str, Any]:
		return self._juego_por_lid[lobby_id].estado()


	def desconectar_jugador(self, jugador: str) -> None:
		if jugador not in self._jugadores():
			raise JugadorInexistenteException()

		lobby = self._lobby_de.pop(jugador)
		lobby.remover_jugador(jugador)

	def _jugadores(self) -> Set[str]:
		return self._lobby_de.keys()

	def _lobbies(self) -> Set[str]:
		return self._lobbies_por_lid.keys()
