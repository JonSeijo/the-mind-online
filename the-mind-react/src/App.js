import React from 'react';
import io from 'socket.io-client'
import IntroView from './IntroView.js';
import LobbyView from './LobbyView.js';
import JuegoView from './JuegoView.js';
import './App.css';

const socket = io("https://jonseijo.com")

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      view: 'IntroView',
      name: ''
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
          name={this.state.name}
          socket={socket}/> );
    }

    if (this.state.view === 'JuegoView') {
      return (
        <JuegoView
          app={this}
          name={this.state.name}
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
