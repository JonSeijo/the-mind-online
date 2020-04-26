# pyre-strict

from typing import Any, Dict, List, Set

from model.lobby import Lobby


class MindControl():

	def __init__(self) -> None:
		self._lobbies_by_name : Dict[str, Lobby] = {}
		self._jugadores : Set[str] = set()

	def agregar_lobby(self, lobby_name: str) -> Lobby:
		if lobby_name in self._lobbies_by_name:
			raise LobbyExistenteException

		lobby = Lobby()
		self._lobbies_by_name[lobby_name] = lobby
		return lobby

	def agregar_jugador(self, jugador: str, lobby: str) -> None:
		if jugador in self._jugadores:
			raise JugadorExistenteException()

		self._jugadores.add(jugador)
		self._lobbies_by_name[lobby].agregar_jugador(jugador)


	def estado_lobby(self, lobby: str) -> Dict[str, Any]:
		return self._lobbies_by_name[lobby].estado()


class LobbyExistenteException(Exception):
	def __init__(self, msg: str ='El lobby ya está completo') -> None:
		super().__init__(msg)


class JugadorExistenteException(Exception):
	def __init__(self, msg: str ='El jugador ya existe en The Mind') -> None:
		super().__init__(msg)
