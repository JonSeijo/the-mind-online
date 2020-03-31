import React from 'react';
import io from 'socket.io-client'
import IntroView from './IntroView.js';
import './App.css';

const socket = io('http://localhost:5000')

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {view: 'IntroView'};
  }

  // useEffect(() => {
    // socket.emit('conectar', {'param': 'esto es un parametro de react'});
    // socket.emit('conectar');
    // socket.on('connect_response', (param) => {
    //   console.log(param)
    //   setCurrentTime(999);
    // });

    // fetch('/time').then(res => res.json()).then(data => {
    //   setCurrentTime(data.time);
    // });
  // }, []);

  render() {
    if (this.state.view === 'IntroView') {
      return ( <IntroView app={this}/> );
    }

    if (this.state.view === 'LobbyView') {
      return ( 'Estoy en el lobby' );
    }


    return (
      <div>
        Che, no encontre { this.state.view }
      </div>
    )
  }
}

export default App;
