# pyre-strict

from typing import Any, Dict, List, KeysView

from model.exceptions import *
from model.lobby import Lobby
from model.juego import Juego


class MindControl():

	def __init__(self) -> None:
		self._lobby_de : Dict[str, str] = {}
		self._lobbies_por_lid : Dict[str, Lobby] = {}
		self._juegos_por_lid : Dict[str, Juego] = {}

	def agregar_lobby(self, lobby_id: str) -> Lobby:
		if lobby_id in self._lobbies_por_lid:
			raise LobbyExistenteException()

		lobby = Lobby()
		self._lobbies_por_lid[lobby_id] = lobby
		return lobby

	def agregar_jugador(self, jugador: str, lobby_id: str) -> None:
		self._assertJugadorInexistente(jugador)
		if lobby_id not in self._lobbies_por_lid:
			self.agregar_lobby(lobby_id)

		lobby = self._lobby_por_lid(lobby_id)

		self._lobby_de[jugador] = lobby_id
		lobby.agregar_jugador(jugador)

	def iniciar_juego_en(self, lobby_id: str) -> None:
		lobby = self._lobby_por_lid(lobby_id)

		self._assertLobbyNoVacio(lobby)
		self._assertJuegoNoEstaEnCurso(lobby_id)

		juego = Juego.iniciar(jugadores=lobby.jugadores())
		self._juegos_por_lid[lobby_id] = juego

	def subir_nivel_en(self, lobby_id: str, force: bool = False) -> None:
		juego = self._juego_por_lid(lobby_id)
		juego.subir_nivel(force)

	def colocar_carta(self, lobby_id: str, jugador: str, carta: int) -> None:
		juego = self._juego_por_lid(lobby_id)
		juego.poner_carta(jugador, carta)


	def estado_lobby(self, lobby_id: str) -> Dict[str, Any]:
		return self._lobby_por_lid(lobby_id).estado()

	def estado_juego(self, lobby_id: str) -> Dict[str, Any]:
		return self._juego_por_lid(lobby_id).estado()

	def estado_juego_por_jug(self, jugador: str) -> Dict[str, Any]:
		lobby_id = self._lobby_de[jugador]
		return self.estado_juego(lobby_id)

	def desconectar_jugador(self, jugador: str) -> None:
		self._assertJugadorExistente(jugador)

		lobby_id = self._lobby_de.pop(jugador)
		lobby = self._lobbies_por_lid[lobby_id]
		lobby.remover_jugador(jugador)

		if lobby_id in self._juegos_por_lid:
			juego = self._juego_por_lid(lobby_id)
			juego.terminar()

		if len(lobby.jugadores()) == 0:
			self._eliminar_lobby(lobby_id)

	def _eliminar_lobby(self, lobby_id: str) -> None:
		self._juegos_por_lid.pop(lobby_id, None)
		self._lobbies_por_lid.pop(lobby_id)

	def _jugadores(self) -> KeysView[str]:
		return self._lobby_de.keys()

	def _lobbies(self) -> KeysView[str]:
		return self._lobbies_por_lid.keys()

	def _lobby_por_lid(self, lobby_id: str) -> Lobby:
		self._assertLobbyExistente(lobby_id)
		return self._lobbies_por_lid[lobby_id]

	def _juego_por_lid(self, lobby_id: str) -> Juego:
		self._assertLobbyExistente(lobby_id)
		self._assertJuegoExistente(lobby_id)
		return self._juegos_por_lid[lobby_id]

	def _assertLobbyExistente(self, lobby_id: str) -> None:
		if lobby_id not in self._lobbies():
			raise LobbyInexistenteException()

	def _assertJuegoExistente(self, lobby_id: str) -> None:
		if lobby_id not in self._juegos_por_lid:
			raise JuegoInexistenteException()

	def _assertJugadorExistente(self, jugador: str) -> None:
		if jugador not in self._jugadores():
			raise JugadorInexistenteException()

	def _assertJugadorInexistente(self, jugador: str) -> None:
		if jugador in self._jugadores():
			raise JugadorExistenteException()

	def _assertLobbyNoVacio(self, lobby: Lobby) -> None:
		if len(lobby.jugadores()) < 2:
			raise LobbyIncompletoException()

	def _assertJuegoNoEstaEnCurso(self, lobby_id: str) -> None:
		if lobby_id in self._juegos_por_lid:
			juego = self._juegos_por_lid[lobby_id]
			if not juego.terminado():
				raise JuegoEnCursoException()


