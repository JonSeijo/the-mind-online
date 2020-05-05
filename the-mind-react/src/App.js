import React from 'react';
import io from 'socket.io-client'
import IntroView from './IntroView.js';
import LobbyView from './LobbyView.js';
import JuegoView from './JuegoView.js';
import './App.css';


const url = process.env.NODE_ENV === "production"
  ? "https://jonseijo.com" : "http://localhost:5000"
const socket = io(url)

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      view: 'IntroView',
      player_name: '',
      lobby_name: '',
    };
  }

  componentDidMount() {
    socket.on('juego_iniciado', () => {
      this.handleJuegoIniciado()
    })
    socket.on('juego_terminado', () => {
      this.handleJuegoTerminado()
    })
  }

  handleJuegoIniciado() {
    console.log('Inicio el juego')
    this.setState({'view': 'JuegoView'})
  }

  handleJuegoTerminado() {
    console.log('Termino el juego')
    this.setState({'view': 'LobbyView'})
  }

  render() {
    if (this.state.view === 'IntroView') {
      return ( <IntroView app={this} socket={socket}/> );
    }

    if (this.state.view === 'LobbyView') {
      return (
        <LobbyView
          app={this}
          player_name={this.state.player_name}
          lobby_name={this.state.lobby_name}
          socket={socket}/> );
    }

    if (this.state.view === 'JuegoView') {
      return (
        <JuegoView
          app={this}
          name={this.state.player_name}
          socket={socket}/>);
    }


    return (
      <div>
        Che, no encontre { this.state.view }
      </div>
    )
  }
}

export default App;
