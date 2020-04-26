# pyre-strict

import unittest

from model.lobby import LobbyCompletoException
from model.mind_control import (
	MindControl,
	LobbyExistenteException,
	JugadorExistenteException
)

class MindControlTest(unittest.TestCase):

	def test_puedo_agregar_lobby_nuevo(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		self.assertEqual({'jugadores': []}, mind.estado_lobby('Kanto'))

	def test_no_puedo_agregar_lobby_existente(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		self.assertRaises(LobbyExistenteException,
			mind.agregar_lobby, 'Kanto')

	def test_puedo_agregar_jugadores_a_un_lobby(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		self.assertEqual({'jugadores': ['Articuno']}, mind.estado_lobby('Kanto'))

	def test_agregar_jugadores_a_un_mismo_lobby_tiene_limite(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		mind.agregar_jugador('Zapdos', 'Kanto')
		mind.agregar_jugador('Moltres', 'Kanto')
		mind.agregar_jugador('Mewtwo', 'Kanto')

		self.assertRaises(LobbyCompletoException,
			mind.agregar_jugador, 'Magikarp', 'Kanto'
		)

	def test_no_puedo_agregar_el_mismo_jugador_a_dos_lobbies(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_lobby('Johto')
		mind.agregar_jugador('Articuno', 'Kanto')

		self.assertRaises(JugadorExistenteException,
			mind.agregar_jugador, 'Articuno', 'Johto'
		)

