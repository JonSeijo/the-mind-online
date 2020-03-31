import React from 'react';
import io from 'socket.io-client'
import IntroView from './IntroView.js';
import LobbyView from './LobbyView.js';
import './App.css';

const socket = io('http://localhost:5000')

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      view: 'IntroView',
      name: ''
    };
  }

  render() {
    if (this.state.view === 'IntroView') {
      return ( <IntroView app={this}/> );
    }

    if (this.state.view === 'LobbyView') {
      return (
        <LobbyView
          app={this}
          name={this.state.name}
          socket={socket}/> );
    }


    return (
      <div>
        Che, no encontre { this.state.view }
      </div>
    )
  }
}

export default App;