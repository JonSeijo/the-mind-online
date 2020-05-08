class LobbyExistenteException(Exception):
	def __init__(self, msg: str ='El lobby ya existe') -> None:
		super().__init__(msg)

class LobbyInexistenteException(Exception):
	def __init__(self, msg: str ='El lobby no existe') -> None:
		super().__init__(msg)

class LobbyCompletoException(Exception):
	def __init__(self, msg: str ='El lobby ya está completo') -> None:
		super().__init__(msg)

class LobbyIncompletoException(Exception):
	def __init__(self, msg: str ='El lobby está incompleto') -> None:
		super().__init__(msg)

class JugadorExistenteException(Exception):
	def __init__(self, msg: str ='El jugador ya existe en The Mind') -> None:
		super().__init__(msg)

class JugadorInexistenteException(Exception):
	def __init__(self, msg: str ='El jugador NO existe en The Mind') -> None:
		super().__init__(msg)

class JuegoEnCursoException(Exception):
	def __init__(self, msg: str ='El juego ya está en curso') -> None:
		super().__init__(msg)

class JuegoTerminadoException(Exception):
	def __init__(self, msg: str ='El juego ya está terminado') -> None:
		super().__init__(msg)

class JuegoInexistenteException(Exception):
	def __init__(self, msg: str ='No existe juego') -> None:
		super().__init__(msg)

class CartaInexistenteException(Exception):
	def __init__(self, msg: str ='La carta es inexistente') -> None:
		super().__init__(msg)

class InvalidNameException(Exception):
	def __init__(self, msg: str ='El nombre es invalido') -> None:
		super().__init__(msg)
