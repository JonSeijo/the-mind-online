import React from 'react'

class LobbyView extends React.Component {

  componentDidMount() {
    this.props.socket.emit('conectar', {});
    this.props.socket.on('conectar_response', (param) => {
      console.log('Conexion con el server: ' + param.status)
    })
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