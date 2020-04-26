# pyre-strict

from typing import Any, Dict, List

from model.exceptions import *

class Lobby():

	def __init__(self) -> None:
		self._jugadores : List[str] = []
		self._capacidad : int = 4

	def agregar_jugador(self, jugador: str) -> None:
		if jugador in self._jugadores:
			raise JugadorExistenteException()

		if len(self._jugadores) >= self._capacidad:
			raise LobbyCompletoException()


		self._jugadores.append(jugador)

	def remover_jugador(self, jugador: str) -> None:
		if jugador not in self._jugadores:
			raise JugadorInexistenteException()

		self._jugadores.remove(jugador)

	def jugadores(self) -> List[str]:
		return self._jugadores

	def estado(self) -> Dict[str, Any]:
		return {
			'jugadores': self.jugadores()
		}

	def reset(self) -> None:
		self._jugadores = []

