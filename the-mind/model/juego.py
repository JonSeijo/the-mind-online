# pyre-strict

import random
from typing import Any, Dict, List

class Juego(object):

	# Usar Juego.iniciar()
	def __init__(self,
		jugadores: List[str] = [],
		mesa: int = 0,
		nivel: int = 0,
		vidas: int = 0,
		cartas_por_jugador: Dict[str, List[int]] = {},
		premios_vidas: List[int] = [],
		terminado: bool = False,
	) -> None:
		self._assert_jugadores_unicos(jugadores)
		self._mesa = mesa
		self._nivel = nivel
		self._vidas = vidas
		self._jugadores = jugadores
		self._cartas_por_jugador = cartas_por_jugador
		self._premios_vidas = premios_vidas
		self._terminado = terminado

	@classmethod
	def iniciar(cls, jugadores: List[str] = []) -> 'Juego':
		return cls.iniciar_en_nivel(jugadores=jugadores, nivel=1)

	@classmethod
	def iniciar_en_nivel(
		cls,
		jugadores: List[str],
		nivel: int
	) -> 'Juego':
		cartas_por_jugador = cartas_repartidas(jugadores, nivel)

		return cls(
			jugadores=jugadores,
			mesa = 0,
			nivel=nivel,
			vidas=3,
			cartas_por_jugador=cartas_por_jugador,
			premios_vidas=[3, 6, 9]
		)


	def nivel(self) -> int:
		return self._nivel

	def subir_nivel(self, force: bool = False) -> None:
		if not force and self._hay_cartas_pendientes():
			raise JuegoEnCursoException()

		if self._nivel in self._premios_vidas:
			self._vidas += 1

		self._mesa = 0
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

		if self.terminado():
			raise JuegoTerminadoException()

		descartadas = self._descartar_toda_carta_no_mayor(carta)
		if len(descartadas) > 1:
			self._vidas -= 1

		self._mesa = carta

	def terminado(self) -> bool:
		return self._terminado or self._vidas <= 0

	def terminar(self) -> None:
		self._terminado = True

	def estado(self) -> Dict[str, Any]:
		return {
			'vidas': self.vidas(),
			'nivel': self.nivel(),
			'mesa': self.mesa(),
			'terminado': self.terminado(),
			'jugadores': self.jugadores(),
			'cartas_por_jugador': self.cartas_por_jugador()
		}

	def _hay_cartas_pendientes(self) -> bool:
		for jugador, cartas in self._cartas_por_jugador.items():
			if len(cartas) > 0:
				return True

		return False

	def _descartar_toda_carta_no_mayor(self, carta_jugada: int) -> List[int]:
		descartadas = []
		for jugador, cartas in self._cartas_por_jugador.items():
			descartadas += [
				carta for carta in cartas
				if carta <= carta_jugada
			]

			self._cartas_por_jugador[jugador] = [
				carta for carta in cartas
				if carta > carta_jugada
			]

		return descartadas

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


class JuegoEnCursoException(Exception):
	pass


class JuegoTerminadoException(Exception):
	pass