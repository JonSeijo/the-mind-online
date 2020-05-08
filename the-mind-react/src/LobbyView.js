import React from 'react'
import './css/Common.css'
import './css/Lobby.css'

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
    this.props.socket.emit('lobby_estado')
  }

  componentWillUnmount() {
    this.props.socket.off('lobby_update')
  }

  handleLobbyUpdate(lobby_state) {
    this.setState({
      'jugadores': lobby_state.jugadores,
      'error_lobby': lobby_state.error,
    })
  }

  render() {
    if (this.state.error_lobby) {
      return "ERROR: " + this.state.error_lobby;
    }

    const jugadoresItems = this.state.jugadores.map((jugador) =>
      <div key={jugador}> {jugador} </div>
    );

    return (
      <div className="LobbyWrapper">
        <div className="LobbyHeader">
          <div className="LobbyName"> {this.props.lobby_name} </div>
          <div className="LobbyJugadoresTitle"> Jugadores </div>
          <div className="LobbyJugadores"> {jugadoresItems} </div>
        </div>
        <div className="LobbyIniciar">
          { this.renderBotonIniciar(this.state.jugadores) }
        </div>
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
      <button
        className="CommonButton"
        onClick={event => this.handleClick(event)}>
        Jugar!
      </button>
    );
  }
}

export default LobbyView;