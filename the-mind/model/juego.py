# pyre-strict

from typing import List

class Juego(object):

	def __init__(self) -> None:
		self._nivel: int = 1
		self._jugadores: List[str] = []

	def nivel(self) -> int:
		return self._nivel

	def subir_nivel(self) -> None:
		self._nivel += 1

	def agregar_jugador(self, jugador: str) -> None:
		if jugador in self._jugadores:
			raise JugadorExistenteException

		self._jugadores.append(jugador)

	def jugadores(self) -> List[str]:
		return self._jugadores


class JugadorExistenteException(Exception):
	pass