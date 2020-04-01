import React from 'react'

class LobbyView extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      'jugadores': [],
      'error': '',
    }
  }

  componentDidMount() {
    this.props.socket.on('lobby_update', (lobby_state) => {
      this.handleLobbyUpdate(lobby_state)
    })

    this.props.socket.emit(
      'agregar_jugador_lobby', {
        'name': this.props.name
      })
  }

  handleLobbyUpdate(lobby_state) {
    console.log('Me llego la info del lobby:')
    console.log(lobby_state)
    this.setState({
      'jugadores': lobby_state.jugadores
    })
  }

  render() {

    if (this.state.error) {
      return "Error" + this.state.error;
    }

    const jugadoresItems = this.state.jugadores.map((jugador) =>
      <li key={jugador}> {jugador} </li>
    );

    return (
      <div>
        <div> Estoy en el lobby. Soy { this.props.name }. </div>
        <div> Los jugadores son: </div>
        <div> <ul>{jugadoresItems}</ul> </div>
      </div>
    )
  }
}

export default LobbyView;