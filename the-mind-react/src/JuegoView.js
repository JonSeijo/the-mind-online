import React from 'react'
import InfoSection from './section/InfoSection.js'
import MesaSection from './section/MesaSection.js'
import ManoSection from './section/ManoSection.js'
import './css/Juego.css'

class JuegoView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'mesa': 0,
      'vidas': 0,
      'cartas': [],
      'cant_cartas_jugadores': {},
    }
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
    let name = this.props.name
    let cartas_por_jugador = juego_state.cartas_por_jugador
    let cartas_mias = cartas_por_jugador[name]
    let cant_cartas_jugadores = {}

    Object.entries(cartas_por_jugador).map(
      ([jug, suscartas]) =>
        cant_cartas_jugadores[jug] = suscartas.length
    )

    // Normal integer sort because javascript
    cartas_mias.sort((a, b) => (a - b));

    this.setState({
      'mesa': juego_state.mesa,
      'vidas': juego_state.vidas,
      'nivel': juego_state.nivel,
      'cartas': cartas_mias,
      'cant_cartas_jugadores': cant_cartas_jugadores
    })
  }

  render() {
    return (
      <div className="WrapperSection">

        <InfoSection
          nivel={this.state.nivel}
          vidas={this.state.vidas}
          cant_cartas_jugadores={this.state.cant_cartas_jugadores}
        />

        <MesaSection mesa={this.state.mesa}/>

        <ManoSection
          socket={this.props.socket}
          vidas={this.state.vidas}
          cartas={this.state.cartas}
          cant_cartas_jugadores={this.state.cant_cartas_jugadores}
        />

      </div>
    )
  }
}

export default JuegoView;