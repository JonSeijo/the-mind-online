import React from 'react'

class LobbyView extends React.Component {

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
  }

  render() {
    let name = this.props.name;

    return (
      <div>
        Estoy en el lobby. Soy { name }
      </div>
    );
  }
}

export default LobbyView;