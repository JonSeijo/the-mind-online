# pyre-strict

import unittest

from typing import Any, Dict, List, Generic, Optional, TypeVar

from model.juego import (
	Juego,
	JugadorExistenteException,
	JugadorInexistenteException,
	CartaInexistenteException,
	JuegoEnCursoException,
	JuegoTerminadoException
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


	def test_avanzar_de_nivel_da_las_vidas_correctas_dos_jugs(self) -> None:
		juego = juego_default()
		gano_vida_al_completar = [3, 6, 9]
		vidas_esperadas = 3
		for nivel_act in range(1, 13):
			juego.subir_nivel(force=True)

			if nivel_act in gano_vida_al_completar:
				vidas_esperadas += 1

			self.assertEqual(vidas_esperadas, juego.vidas(), f'en nivel {nivel_act}')


	def test_jugar_incorrectamente_pierde_vidas(self) -> None:
		juego = juego_default()
		self.assertEqual(3, juego.vidas())
		juego.poner_carta('Articuno', 3)
		self.assertEqual(2, juego.vidas())


	def test_no_puedo_colocar_cartas_si_no_tengo_vidas(self) -> None:
		juego = juego_sin_vidas()
		self.assertRaises(JuegoTerminadoException,
			juego.poner_carta, 'Articuno', 1)


	def test_juego_en_curso_si_no_perdi(self) -> None:
		juego = juego_con_vidas(1)
		self.assertFalse(juego.terminado())

		juego.poner_carta('Articuno', 3)
		self.assertTrue(juego.terminado())


	def test_juego_termina_forzosamente(self) -> None:
		juego = juego_default()
		self.assertFalse(juego.terminado())

		juego.terminar()
		self.assertTrue(juego.terminado())


	def test_juego_no_pone_carta_si_termino_forzosamente(self) -> None:
		juego = juego_default()
		juego.terminar()
		self.assertRaises(JuegoTerminadoException,
			juego.poner_carta, 'Articuno', 1)


	def test_estado_del_juego(self) -> None:
		juego = juego_default()
		self.assertEqual(
			{
				'nivel': 1,
				'mesa': 0,
				'vidas': 3,
				'terminado': False,
				'jugadores': ['Articuno', 'Zapdos'],
				'cartas_por_jugador': {
					'Articuno': [1, 3],
					'Zapdos': [2, 4]
				},
			}
			, juego.estado())

	def assertUnique(self, elems: List[int]) -> None:
		self.assertEqual(len(elems), len(set(elems)))


def crear_juego_test(
	jugadores : Optional[List[str]] = None,
	mesa : Optional[int] = None,
	nivel : Optional[int] = None,
	vidas : Optional[int] = None,
	cartas_por_jugador : Optional[Dict[str, List[int]]] = None,
	premios_vidas : Optional[List[int]] = None
) -> Juego:

	return Juego(
		jugadores = ordefault(jugadores, ['Articuno', 'Zapdos']),
		mesa = ordefault(mesa, 0),
		nivel = ordefault(nivel, 1),
		vidas = ordefault(vidas, 3),
		cartas_por_jugador = ordefault(cartas_por_jugador, {
			'Articuno': [1, 3],
			'Zapdos': [2, 4]
		}),
		premios_vidas = ordefault(premios_vidas, [3, 6, 9])
	)


def juego_default() -> Juego:
	return crear_juego_test()


def juego_sin_cartas() -> Juego:
	return crear_juego_test(cartas_por_jugador={})


def juego_sin_vidas() -> Juego:
	return crear_juego_test(vidas=0)

def juego_con_vidas(vidas: int) -> Juego:
	return crear_juego_test(vidas=vidas)

# pyre-ignore
def ordefault(custom: Any, default: Any) -> Any:
	return default if custom is None else custom