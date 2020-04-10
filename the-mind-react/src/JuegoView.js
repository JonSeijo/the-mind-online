import React from 'react'

class JuegoView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'mesa': -1,
      'vidas': 0,
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

    Object.entries(cartas_por_jugador).map(
      ([jug, suscartas]) =>
        jugadores_cantidades[jug] = suscartas.length
    )

    // Normal integer sort because javascript
    cartas_mias.sort((a, b) => (a - b));

    this.setState({
      'mesa': juego_state.mesa,
      'vidas': juego_state.vidas,
      'cartas': cartas_mias,
      'jugadores_cantidades': jugadores_cantidades
    })
  }

  render() {

    let cartasItems = []
    let cartasRestantes = []
    let cuentaCartasRestantes = 0

    if (this.state.cartas) {
      cartasItems = this.state.cartas.map((carta) =>
        <Carta key={carta}
          valor={carta}
          socket={this.props.socket}/>
      );
    }

    if (this.state.jugadores_cantidades) {
      cartasRestantes = Object.entries(this.state.jugadores_cantidades)
        .map( ([jug, cant]) =>
          <li key={jug}> {jug + ": " + cant} </li>)

      Object.entries(this.state.jugadores_cantidades)
        .forEach( ([jug, cant]) => {cuentaCartasRestantes += cant} )
    }

    return (
      <div>
        <div> Estoy en el JUEGO. </div>
        <div> La carta en la mesa es: {this.state.mesa} </div>
        <br/>
        <div> Mis cartas son: </div>
        <div> {cartasItems} </div>
        <br/>
        <div> VIDAS: </div>
        <div> {this.state.vidas} </div>
        <br/>
        <div> Cant de cartas restantes: </div>
        <div> <ul>{cartasRestantes}</ul> </div>
        <br/>
        { this.botonSiguienteNivel(cuentaCartasRestantes) }
        { this.botonGameOver(this.state.vidas) }
      </div>
    )
  }

  botonSiguienteNivel(cantRestantes) {
    return cantRestantes ? null : (
      <div>
        <button
         onClick={event => {
          event.preventDefault();
          this.props.socket.emit('subir_nivel');
         }}>
          SIGUIENTE NIVEL
        </button>
      </div>
    )
  }

  botonGameOver(vidas) {
    return vidas ? null : (
      <div>
        <button
         onClick={event => {
          event.preventDefault();
          this.props.socket.emit('juego_quiero_terminar');
         }}>
          GAME OVER
        </button>
      </div>
    )
  }
}

class Carta extends React.Component {

  handleClick(event) {
    event.preventDefault();
    this.props.socket.emit('poner_carta',
      {'carta': this.props.valor}
    );
  }

  render() {
    return (
      <div>
        <div>{this.props.valor}</div>
        <div>
          <button onClick={event => this.handleClick(event)}> Poner </button>
        </div>
      </div>
    )
  }
}

export default JuegoView;