import React from 'react'

class LobbyView extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      'jugadores': [],
      'error_lobby': '',
    }
  }

  componentDidMount() {
    this.props.socket.on('lobby_update', (lobby_state) => {
      this.handleLobbyUpdate(lobby_state)
    })

    this.props.socket.on('juego_iniciado', () => {
      this.handleJuegoIniciado()
    })

    this.props.socket.emit(
      'lobby_agregar_jugador', {
        'name': this.props.name
      })
  }

  handleLobbyUpdate(lobby_state) {
    console.log('Me llego la info del lobby:')
    console.log(lobby_state)
    this.setState({
      'jugadores': lobby_state.jugadores,
      'error_lobby': lobby_state.error,
    })
  }

  handleJuegoIniciado() {
    console.log('Quiero iniciar el juego')
    this.props.app.setState({
      'view': 'JuegoView'
    })
  }

  render() {
    if (this.state.error_lobby) {
      return "ERROR: " + this.state.error_lobby;
    }

    const jugadoresItems = this.state.jugadores.map((jugador) =>
      <li key={jugador}> {jugador} </li>
    );

    return (
      <div>
        <div> Estoy en el lobby. Soy { this.props.name }. </div>
        <div> Los jugadores son: </div>
        <div> <ul>{jugadoresItems}</ul> </div>
        { this.renderBotonIniciar(this.state.jugadores) }
      </div>
    )
  }

  renderBotonIniciar(jugadores) {
    return jugadores && jugadores.length > 1
      ? (<div> <BotonIniciarJuego socket={this.props.socket}/> </div>)
      : null;
  }
}

class BotonIniciarJuego extends React.Component {

  handleClick(event) {
    event.preventDefault();
    this.props.socket.emit('juego_iniciar');
  }

  render() {
    return (
      <button onClick={event => this.handleClick(event)}>
        Jugar!
      </button>
    );
  }
}

export default LobbyView;