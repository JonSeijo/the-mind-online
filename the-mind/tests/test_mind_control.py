# pyre-strict

import unittest

from model.lobby import LobbyCompletoException
from model.mind_control import (
	MindControl,
	LobbyExistenteException,
	LobbyIncompletoException,
	LobbyInexistenteException,
	JuegoEnCursoException,
	JugadorExistenteException,
	JugadorInexistenteException
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

	def test_jugador_se_desconecta_correctamente(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		mind.desconectar_jugador('Articuno')
		self.assertEqual({'jugadores': []}, mind.estado_lobby('Kanto'))

	def test_no_puedo_desconectar_un_jugador_inexistente(self) -> None:
		mind = MindControl()
		self.assertRaises(JugadorInexistenteException,
			mind.desconectar_jugador, 'Articuno'
		)

	def test_no_puedo_agregar_jugador_a_lobby_inexistente(self) -> None:
		mind = MindControl()
		self.assertRaises(LobbyInexistenteException,
			mind.agregar_jugador, 'Articuno', 'Kanto'
		)

	def test_puedo_agregar_jugador_preexistente_si_desconecto_previamente(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		mind.desconectar_jugador('Articuno')
		mind.agregar_jugador('Articuno', 'Kanto')
		self.assertEqual({'jugadores': ['Articuno']}, mind.estado_lobby('Kanto'))


	def test_estado_de_lobby_inexistente_da_error(self) -> None:
		mind = MindControl()
		self.assertRaises(LobbyInexistenteException,
			mind.estado_lobby, 'Kanto')


	def test_iniciar_juego_en_lobby(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		mind.agregar_jugador('Zapdos', 'Kanto')
		mind.iniciar_juego_en('Kanto')
		self.assertFalse(mind.estado_juego('Kanto')['terminado'])


	def test_no_puedo_iniciar_un_juego_ya_iniciado(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		mind.agregar_jugador('Zapdos', 'Kanto')
		mind.iniciar_juego_en('Kanto')

		self.assertRaises(JuegoEnCursoException,
			mind.iniciar_juego_en, 'Kanto'
		)

	def test_no_puedo_iniciar_juego_en_lobby_inexistente(self) -> None:
		mind = MindControl()
		self.assertRaises(LobbyInexistenteException,
			mind.iniciar_juego_en, 'Kanto'
		)

	def test_no_puedo_iniciar_juego_en_lobby_incompleto(self) -> None:
		mind = MindControl()
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		self.assertRaises(LobbyIncompletoException,
			mind.iniciar_juego_en, 'Kanto'
		)
