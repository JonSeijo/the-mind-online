# pyre-strict

import random
from typing import Dict, List

class Juego(object):

	def __init__(self, jugadores: List[str] = []) -> None:
		self._assert_jugadores_unicos(jugadores)
		self._nivel: int = 1
		self._jugadores: List[str] = jugadores
		self._repartir_cartas()

	def nivel(self) -> int:
		return self._nivel

	def subir_nivel(self) -> None:
		self._nivel += 1
		self._repartir_cartas()

	def jugadores(self) -> List[str]:
		return self._jugadores

	def cartas_por_jugador(self) -> Dict[str, List[int]]:
		return self._cartas_por_jugador

	def _assert_jugadores_unicos(self, jugadores: List[str]) -> None:
		if len(jugadores) != len(set(jugadores)):
			raise JugadorExistenteException

	def _repartir_cartas(self) -> None:
		mazo = self._mazo_mezclado()
		self._cartas_por_jugador: Dict[str, List[int]] = {}

		for jug_idx, jug in enumerate(self.jugadores()):
			inicio = jug_idx * self.nivel()
			fin = inicio + self.nivel()
			self._cartas_por_jugador[jug] = mazo[inicio:fin]

	def _mazo_mezclado(self) -> List[int]:
		mazo = [ i for i in range(1, 101) ]
		random.shuffle(mazo)
		return mazo

class JugadorExistenteException(Exception):
	pass