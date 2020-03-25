# pyre-strict

import unittest

from model.juego import Juego, JugadorExistenteException

class JuegoTest(unittest.TestCase):

	def test_juego_empieza_nivel_uno(self) -> None:
		juego = Juego()
		self.assertEqual(1, juego.nivel())


	def test_juego_sube_nivel_correctamente(self) -> None:
		juego = Juego()
		juego.subir_nivel()
		juego.subir_nivel()
		self.assertEqual(3, juego.nivel())


	def test_juego_registra_jugadores(self) -> None:
		juego = Juego()
		juego.agregar_jugador('Articuno')
		juego.agregar_jugador('Zapdos')

		jugadores = juego.jugadores()
		self.assertIn('Articuno', jugadores)
		self.assertIn('Zapdos', jugadores)
		self.assertEqual(2, len(jugadores))


	def test_juego_no_agrega_jugadores_repetidos(self) -> None:
		juego = Juego()
		juego.agregar_jugador('Moltres')

		self.assertRaises(
			JugadorExistenteException,
			juego.agregar_jugador, 'Moltres'
		)
