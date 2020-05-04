# pyre-strict

import unittest

from model.exceptions import *
from model.lobby import LobbyCompletoException
from model.mind_control import MindControl


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
		mind = mind_con_un_jugador()
		self.assertEqual({'jugadores': ['Articuno']}, mind.estado_lobby('Kanto'))

	def test_agregar_jugadores_a_un_mismo_lobby_tiene_limite(self) -> None:
		mind = mind_con_un_jugador()
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
		mind = mind_juego_iniciado()
		mind.desconectar_jugador('Articuno')
		self.assertEqual({'jugadores': ['Zapdos']}, mind.estado_lobby('Kanto'))

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
		mind = mind_con_un_jugador()
		mind.desconectar_jugador('Articuno')
		mind.agregar_lobby('Kanto')
		mind.agregar_jugador('Articuno', 'Kanto')
		self.assertEqual({'jugadores': ['Articuno']}, mind.estado_lobby('Kanto'))


	def test_estado_de_lobby_inexistente_da_error(self) -> None:
		mind = MindControl()
		self.assertRaises(LobbyInexistenteException,
			mind.estado_lobby, 'Kanto')

	def test_iniciar_juego_en_lobby(self) -> None:
		mind = mind_juego_iniciado()
		self.assertFalse(mind.estado_juego('Kanto')['terminado'])

	def test_no_puedo_iniciar_un_juego_ya_iniciado(self) -> None:
		mind = mind_juego_iniciado()

		self.assertRaises(JuegoEnCursoException,
			mind.iniciar_juego_en, 'Kanto'
		)

	def test_no_puedo_iniciar_juego_en_lobby_inexistente(self) -> None:
		mind = MindControl()
		self.assertRaises(LobbyInexistenteException,
			mind.iniciar_juego_en, 'Kanto'
		)

	def test_no_puedo_iniciar_juego_en_lobby_incompleto(self) -> None:
		mind = mind_con_un_jugador()
		self.assertRaises(LobbyIncompletoException,
			mind.iniciar_juego_en, 'Kanto'
		)

	def test_desconectar_jugador_termina_el_juego(self) -> None:
		mind = mind_juego_iniciado()

		self.assertFalse(mind.estado_juego('Kanto')['terminado'])
		mind.desconectar_jugador('Articuno')
		self.assertTrue(mind.estado_juego('Kanto')['terminado'])

	def test_desconectar_el_ultimo_jugador_elimina_el_lobby(self) -> None:
		mind = mind_juego_iniciado()
		mind.desconectar_jugador('Articuno')
		self.assertTrue(mind.estado_juego('Kanto')['terminado'])
		mind.desconectar_jugador('Zapdos')
		self.assertRaises(LobbyInexistenteException,
			mind.estado_lobby, 'Kanto'
		)

	def test_puedo_subir_de_nivel_correctamente(self) -> None:
		mind = mind_juego_iniciado()

		self.assertEqual(1, mind.estado_juego('Kanto')['nivel'])
		mind.subir_nivel_en('Kanto', force=True)
		self.assertEqual(2, mind.estado_juego('Kanto')['nivel'])

		self.assertRaises(
			JuegoEnCursoException,
			mind.subir_nivel_en, 'Kanto'
		)

	def test_estado_juego_dado_jugador(self) -> None:
		mind = mind_juego_iniciado()
		self.assertFalse(mind.estado_juego_por_jug('Zapdos')['terminado'])

	def test_colocar_carta_lobby_incorrecto(self) -> None:
		mind = mind_juego_iniciado()
		self.assertRaises(LobbyInexistenteException,
			mind.colocar_carta, 'LobbyInexistente', 'Articuno', 1
		)

	def test_colocar_carta_jugador_incorrecto(self) -> None:
		mind = mind_juego_iniciado()
		self.assertRaises(JugadorInexistenteException,
			mind.colocar_carta, 'Kanto', 'Magikarp', 1
		)


def mind_con_un_jugador() -> MindControl:
	mind = MindControl()
	mind.agregar_lobby('Kanto')
	mind.agregar_jugador('Articuno', 'Kanto')
	return mind


def mind_juego_iniciado() -> MindControl:
	mind = MindControl()
	mind.agregar_lobby('Kanto')
	mind.agregar_jugador('Articuno', 'Kanto')
	mind.agregar_jugador('Zapdos', 'Kanto')
	mind.iniciar_juego_en('Kanto')
	return mind