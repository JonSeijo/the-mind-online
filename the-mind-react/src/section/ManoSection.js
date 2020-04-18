import React from 'react'
import './SectionStyles.css'

class ManoSection extends React.Component {

  render() {

    let cartasElems = this.buildCartasElems()
    let cartasRestantesCount = this.countCartasRestantes()

    return (
      <div className="ManoSection">
        <div> Mano: {cartasElems} </div>
        { this.botonSiguienteNivel(cartasRestantesCount) }
        { this.botonGameOver(this.props.vidas) }
      </div>
    )
  }

  buildCartasElems() {
    if (!this.props.cartas) {
      return []
    }

    return this.props.cartas.map((carta) =>
      <Carta key={carta}
        valor={carta}
        socket={this.props.socket}/>
    );
  }

  countCartasRestantes() {
    let cartasCount = 0
    if (this.props.cant_cartas_jugadores) {
      Object.entries(this.props.cant_cartas_jugadores)
        .forEach( ([jug, cant]) =>
          {cartasCount += cant} )
    }
    return cartasCount
  }

  botonSiguienteNivel(cantRestantes) {
    return cantRestantes ? null : buttonEmiter(this.props.socket,
      'SIGUIENTE NIVEL', 'subir_nivel')
  }

  botonGameOver(vidas) {
    return vidas ? null : buttonEmiter(this.props.socket,
      'GAME OVER', 'juego_quiero_terminar')
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
        <div> {buttonEmiter(this.props.socket,
            'Poner', 'poner_carta', {'carta': this.props.valor})}
        </div>
      </div>
    )
  }
}

function buttonEmiter(socket, button_text, emit_msg, emit_params) {
  return (
    <button onClick={event => {
      event.preventDefault();
      if (emit_params) {
        socket.emit(emit_msg, emit_params);
      } else {
        socket.emit(emit_msg);
      }
     }}>
      {button_text}
    </button>)
}

export default ManoSection;