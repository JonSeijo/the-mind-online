import React from 'react'

class JuegoView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'mesa': -1,
      'cartas': [],
      'jugadores_cantidades': {},
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
    let jugadores_cantidades = {}

    console.log("cartas_por_jugador")
    console.log(cartas_por_jugador)

    Object.entries(cartas_por_jugador).map(
      ([jug, suscartas]) =>
        jugadores_cantidades[jug] = suscartas.length
    )

    console.log("jugadores_cantidades")
    console.log(jugadores_cantidades)

    this.setState({
      'mesa': juego_state.mesa,
      'cartas': cartas_mias,
      'jugadores_cantidades': jugadores_cantidades
    })
  }

  render() {

    let cartasItems = []
    let cartasRestantes = []

    if (this.state.cartas) {
      cartasItems = this.state.cartas.map((carta) =>
        <li key={carta}> {carta} </li>
      );
    }

    if (this.state.jugadores_cantidades) {
      cartasRestantes = Object.entries(this.state.jugadores_cantidades)
        .map( ([jug, cant]) =>
          <li key={jug}> {jug + ": " + cant} </li>)
    }

    return (
      <div>
        <div> Estoy en el JUEGO. </div>
        <div> La carta en la mesa es: {this.state.mesa} </div>
        <br/>
        <div> Mis cartas son: </div>
        <div> <ul>{cartasItems}</ul> </div>
        <br/>
        <div> Cant de cartas restantes: </div>
        <div> <ul>{cartasRestantes}</ul> </div>
      </div>
    )
  }
}

export default JuegoView;