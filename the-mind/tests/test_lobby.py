# pyre-strict

import unittest

from model.exceptions import *
from model.lobby import Lobby


class LobbyTest(unittest.TestCase):

	def test_lobby_agrega_jugadores_correctamente(self) -> None:
		lobby = Lobby()
		lobby.agregar_jugador('Articuno')
		self.assertIn('Articuno', lobby.jugadores())

		lobby.agregar_jugador('Zapdos')
		self.assertIn('Articuno', lobby.jugadores())
		self.assertIn('Zapdos', lobby.jugadores())

	def test_lobby_no_agrega_jugador_existente(self) -> None:
		lobby = Lobby()
		lobby.agregar_jugador('Articuno')
		self.assertRaises(JugadorExistenteException,
			lobby.agregar_jugador, 'Articuno')

	def test_jugador_puede_salir_del_lobby(self) -> None:
		lobby = Lobby()
		lobby.agregar_jugador('Articuno')
		self.assertIn('Articuno', lobby.jugadores())
		lobby.remover_jugador('Articuno')
		self.assertNotIn('Articuno', lobby.jugadores())

	def test_jugador_inexistente_no_puede_salir_del_lobby(self) -> None:
		lobby = Lobby()
		self.assertRaises(JugadorInexistenteException,
			lobby.remover_jugador, 'Articuno')

	def test_lobby_muestra_estado_correctamente(self) -> None:
		lobby = Lobby()
		lobby.agregar_jugador('Articuno')
		lobby.agregar_jugador('Zapdos')
		self.assertEqual(
			{'jugadores': ['Articuno', 'Zapdos']},
			lobby.estado()
		)

	def test_lobby_resetea_correctamente(self) -> None:
		lobby = Lobby()
		lobby.agregar_jugador('Articuno')
		lobby.agregar_jugador('Zapdos')

		lobby.reset()
		self.assertEqual({'jugadores': []}, lobby.estado())

	def test_lobby_tiene_limite_de_jugadores(self) -> None:
		lobby = Lobby()
		lobby.agregar_jugador('Articuno')
		lobby.agregar_jugador('Zapdos')
		lobby.agregar_jugador('Moltres')
		lobby.agregar_jugador('Mewtwo')

		self.assertRaises(LobbyCompletoException,
			lobby.agregar_jugador, 'Magikarp')

