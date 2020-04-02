# pyre-strict

from typing import List


class Lobby():

	def __init__(self) -> None:
		self._jugadores : List[str] = []

	def agregar_jugador(self, jugador: str) -> None:
		if jugador in self._jugadores:
			raise JugadorExistenteException()

		self._jugadores.append(jugador)

	def remover_jugador(self, jugador: str) -> None:
		if jugador not in self._jugadores:
			raise JugadorInexistenteException()

		self._jugadores.remove(jugador)

	def jugadores(self) -> List[str]:
		return self._jugadores

	def estado(self) -> List[str]:
		return {
			'jugadores': self.jugadores()
		}

	def reset(self) -> None:
		self._jugadores = []

class JugadorExistenteException(Exception):
    def __init__(self, msg='El jugador ya esta en el lobby', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class JugadorInexistenteException(Exception):
	pass
