# pyre-strict

import unittest

from typing import List

from model.juego import (
	Juego,
	JugadorExistenteException,
	JugadorInexistenteException,
	CartaInexistenteException,
	JuegoEnCursoException
)


def juego_default() -> Juego:
	return Juego(
		jugadores = ['Articuno', 'Zapdos'],
		mesa = 0,
		nivel = 1,
		vidas = 3,
		cartas_por_jugador = {
			'Articuno': [1, 3],
			'Zapdos': [2, 4]
		}
	)

def juego_sin_cartas() -> Juego:
	return Juego(
		jugadores = ['Articuno', 'Zapdos'],
		mesa = 0,
		nivel = 1,
		vidas = 3,
		cartas_por_jugador = {}
	)

class JuegoTest(unittest.TestCase):

	def test_juego_empieza_nivel_uno(self) -> None:
		juego = juego_default()
		self.assertEqual(1, juego.nivel())


	def test_juego_sube_nivel_correctamente(self) -> None:
		juego = Juego.iniciar_en_nivel(jugadores=['Articuno', 'Zapdos'], nivel=3)
		self.assertEqual(3, juego.nivel())


	def test_juego_registra_jugadores(self) -> None:
		juego = Juego.iniciar(jugadores=['Articuno', 'Zapdos'])
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
		juego = Juego.iniciar(jugadores=['Articuno', 'Zapdos'])
		cartas_de = juego.cartas_por_jugador()
		self.assertEqual(1, len(cartas_de['Articuno']))
		self.assertEqual(1, len(cartas_de['Zapdos']))


	def test_jugadores_tienen_cartas_igual_nivel(self) -> None:
		juego = Juego.iniciar_en_nivel(jugadores=['Articuno', 'Zapdos'], nivel=3)
		cartas_de = juego.cartas_por_jugador()
		self.assertEqual(3, len(cartas_de['Articuno']))
		self.assertEqual(3, len(cartas_de['Zapdos']))


	def test_jugadores_tienen_cartas_distintas(self) -> None:
		juego = Juego.iniciar_en_nivel(jugadores=['Articuno', 'Zapdos'], nivel=3)
		cartas_de = juego.cartas_por_jugador()

		cartas_todas = [
			carta for jug, cartas in cartas_de.items()
			for carta in cartas
		]

		self.assertUnique(cartas_todas)


	def test_comienzo_tres_vidas(self) -> None:
		juego = juego_default()
		self.assertEqual(3, juego.vidas())


	def test_juego_comienza_con_mesa_cero(self) -> None:
		juego = juego_default()
		self.assertEqual(0, juego.mesa())


	def test_mesa_cambia_cuando_jugador_juega(self) -> None:
		juego = juego_default()
		self.assertEqual(0, juego.mesa())
		juego.poner_carta('Articuno', 1)
		self.assertEqual(1, juego.mesa())
		juego.poner_carta('Zapdos', 2)
		self.assertEqual(2, juego.mesa())


	def test_jugador_pierde_la_carta_luego_de_jugar(self) -> None:
		juego = juego_default()
		self.assertIn(1, juego.cartas_por_jugador()['Articuno'])
		juego.poner_carta('Articuno', 1)
		self.assertNotIn(1, juego.cartas_por_jugador()['Articuno'])


	def test_jugador_inexistente_no_puede_poner_carta(self) -> None:
		juego = juego_default()
		self.assertRaises(
			JugadorInexistenteException,
			juego.poner_carta, 'Moltres', 3
		)


	def test_jugador_no_puede_poner_carta_inexistente(self) -> None:
		juego = juego_default()
		self.assertRaises(
			CartaInexistenteException,
			juego.poner_carta, 'Articuno', 200
		)


	def test_jugador_juega_alta_todos_descartan_las_menores(self) -> None:
		juego = juego_default()
		self.assertIn(1, juego.cartas_por_jugador()['Articuno'])
		self.assertIn(2, juego.cartas_por_jugador()['Zapdos'])

		juego.poner_carta('Articuno', 3)

		self.assertNotIn(1, juego.cartas_por_jugador()['Articuno'])
		self.assertNotIn(2, juego.cartas_por_jugador()['Zapdos'])


	def test_no_puedo_subir_de_nivel_si_hay_cartas_pendientes(self) -> None:
		juego = juego_default()
		self.assertRaises(JuegoEnCursoException, juego.subir_nivel)


	def test_avanzar_de_nivel_da_la_recompensa_correcta(self) -> None:
		pass


	def test_jugar_incorrectamente_pierde_vidas(self) -> None:
		pass


	def test_no_puedo_colocar_cartas_si_no_tengo_vidas(self) -> None:
		pass



	def assertUnique(self, elems: List[int]) -> None:
		self.assertEqual(len(elems), len(set(elems)))
