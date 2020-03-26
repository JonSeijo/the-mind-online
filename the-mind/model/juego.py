# pyre-strict

import random
from typing import Dict, List

class Juego(object):

	# Usar Juego.iniciar()
	def __init__(self,
		jugadores: List[str] = [],
		mesa: int = 0,
		nivel: int = 0,
		vidas: int = 0,
		cartas_por_jugador: Dict[str, List[int]] = {}
	) -> None:
		self._assert_jugadores_unicos(jugadores)
		self._mesa = mesa
		self._nivel = nivel
		self._vidas = vidas
		self._jugadores: List[str] = jugadores
		self._cartas_por_jugador = cartas_por_jugador

	@classmethod
	def iniciar(cls, jugadores: List[str] = []) -> 'Juego':

		nivel_inicial = 1
		cartas_por_jugador = cartas_repartidas(jugadores, nivel_inicial)

		return cls(
			jugadores=jugadores,
			mesa = 0,
			nivel=nivel_inicial,
			vidas=3,
			cartas_por_jugador=cartas_por_jugador
		)

	def nivel(self) -> int:
		return self._nivel

	def subir_nivel(self) -> None:
		self._nivel += 1
		self._repartir_cartas()

	def jugadores(self) -> List[str]:
		return self._jugadores

	def vidas(self) -> int:
		return self._vidas

	def cartas_por_jugador(self) -> Dict[str, List[int]]:
		return self._cartas_por_jugador

	def mesa(self) -> int:
		return self._mesa

	def poner_carta(self, jugador: str, carta: int) -> None:
		if jugador not in self._cartas_por_jugador:
			raise JugadorInexistenteException()

		if carta not in self._cartas_por_jugador[jugador]:
			raise CartaInexistenteException()

		self._cartas_por_jugador[jugador].remove(carta)
		self._mesa = carta

	def _assert_jugadores_unicos(self, jugadores: List[str]) -> None:
		if len(jugadores) != len(set(jugadores)):
			raise JugadorExistenteException

	def _repartir_cartas(self) -> None:
		self._cartas_por_jugador = cartas_repartidas(self.jugadores(), self.nivel())


def mazo_mezclado() -> List[int]:
	mazo = [ i for i in range(1, 101) ]
	random.shuffle(mazo)
	return mazo

def cartas_repartidas(jugadores: List[str], nivel: int) -> Dict[str, List[int]]:
	mazo = mazo_mezclado()
	cartas: Dict[str, List[int]] = {}

	for jug_idx, jug in enumerate(jugadores):
		inicio = jug_idx * nivel
		fin = inicio + nivel
		cartas[jug] = mazo[inicio:fin]

	return cartas



class JugadorExistenteException(Exception):
	pass


class JugadorInexistenteException(Exception):
	pass


class CartaInexistenteException(Exception):
	pass