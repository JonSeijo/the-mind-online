import React from 'react'

class JuegoView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {'mesa': null}
  }

  componentDidMount() {
    this.props.socket.on('juego_update', (juego_state) => {
      this.handleJuegoUpdate(juego_state)
    })
    this.props.socket.emit('juego_estado')
  }

  componentWillUnmount() {
    this.props.socket.off('juego_update')
  }


  handleJuegoUpdate(juego_state) {
    this.setState({
      'mesa': juego_state.mesa
    })
  }

  render() {
    return (
      <div>
        <div> Estoy en el JUEGO. </div>
        <div> La mesa es: {this.state.mesa} </div>
      </div>
    )
  }
}

export default JuegoView;