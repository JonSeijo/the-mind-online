# pyre-strict

from typing import Any, Dict, List, Set

from model.lobby import Lobby


class MindControl():

	def __init__(self) -> None:
		self._jugadores : Set[str] = set()
		self._lobby_de : Dict[str, Lobby] = {}
		self._lobbies_por_nombre : Dict[str, Lobby] = {}

	def agregar_lobby(self, lobby_name: str) -> Lobby:
		if lobby_name in self._lobbies_por_nombre:
			raise LobbyExistenteException

		lobby = Lobby()
		self._lobbies_por_nombre[lobby_name] = lobby
		return lobby

	def agregar_jugador(self, jugador: str, lobby_nombre: str) -> None:
		if jugador in self._jugadores:
			raise JugadorExistenteException()

		lobby = self._lobbies_por_nombre[lobby_nombre]
		self._lobby_de[jugador] = lobby
		lobby.agregar_jugador(jugador)
		self._jugadores.add(jugador)


	def estado_lobby(self, lobby: str) -> Dict[str, Any]:
		return self._lobbies_por_nombre[lobby].estado()

	def desconectar_jugador(self, jugador: str) -> None:
		self._lobby_de[jugador].remover_jugador(jugador)


class LobbyExistenteException(Exception):
	def __init__(self, msg: str ='El lobby ya está completo') -> None:
		super().__init__(msg)


class JugadorExistenteException(Exception):
	def __init__(self, msg: str ='El jugador ya existe en The Mind') -> None:
		super().__init__(msg)
