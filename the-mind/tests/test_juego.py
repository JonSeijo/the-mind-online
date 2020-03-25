# pyre-strict

import unittest

from model.juego import Juego, JugadorExistenteException

def juego_default() -> Juego:
	return Juego(jugadores=['Articuno', 'Zapdos'])

class JuegoTest(unittest.TestCase):

	def test_juego_empieza_nivel_uno(self) -> None:
		juego = juego_default()
		self.assertEqual(1, juego.nivel())


	def test_juego_sube_nivel_correctamente(self) -> None:
		juego = juego_default()
		juego.subir_nivel()
		juego.subir_nivel()
		self.assertEqual(3, juego.nivel())


	def test_juego_registra_jugadores(self) -> None:
		juego = Juego(jugadores=['Articuno', 'Zapdos'])
		jugadores = juego.jugadores()

		self.assertIn('Articuno', jugadores)
		self.assertIn('Zapdos', jugadores)
		self.assertEqual(2, len(jugadores))


	def test_juego_no_registra_jugadores_repetidos(self) -> None:
		self.assertRaises(
			JugadorExistenteException,
			Juego, jugadores=['Moltres', 'Moltres']
		)

	def test_jugadores_tienen_una_carta_al_inicio(self) -> None:
		juego = Juego(jugadores=['Articuno', 'Zapdos'])
		cartas_de = juego.cartas_por_jugador()
		self.assertEqual(1, len(cartas_de['Articuno']))
		self.assertEqual(1, len(cartas_de['Zapdos']))


	def test_jugadores_tienen_cartas_igual_nivel(self) -> None:
		juego = Juego(jugadores=['Articuno', 'Zapdos'])
		juego.subir_nivel()
		juego.subir_nivel()
		cartas_de = juego.cartas_por_jugador()
		self.assertEqual(3, len(cartas_de['Articuno']))
		self.assertEqual(3, len(cartas_de['Zapdos']))


	def test_jugadores_tienen_cartas_distintas(self) -> None:
		juego = Juego(jugadores=['Articuno', 'Zapdos'])
		juego.subir_nivel()
		juego.subir_nivel()
		cartas_de = juego.cartas_por_jugador()

		cartas_todas = [
			carta for jug, cartas in cartas_de.items()
			for carta in cartas
		]

		self.assertUnique(cartas_todas)


	def assertUnique(self, elems) -> None:
		self.assertEqual(len(elems), len(set(elems)))
