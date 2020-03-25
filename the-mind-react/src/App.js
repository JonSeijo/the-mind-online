import React , { useState, useEffect } from 'react';
import io from 'socket.io-client'
import logo from './logo.svg';
import './App.css';

const socket = io('http://localhost:5000')

function App() {

  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    socket.emit('connect');
    socket.on('connect_response', () => {
      setCurrentTime(999);
    });

    // fetch('/time').then(res => res.json()).then(data => {
    //   setCurrentTime(data.time);
    // });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>La hora actual es: {currentTime}</p>
      </header>
    </div>
  );
}

export default App;
