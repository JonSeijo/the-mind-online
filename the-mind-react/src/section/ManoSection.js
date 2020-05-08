import React from 'react'
import '../css/Common.css'
import '../css/Juego.css'

class ManoSection extends React.Component {

  render() {
    return (
      <div className="ManoSection">
        { this.renderCartasElems() }
        { this.renderBotonSiguienteNivel() }
        { this.renderBotonGameOver() }
      </div>
    )
  }

  renderCartasElems() {
    if (!this.props.cartas || this._gameOver()) {
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

  renderBotonSiguienteNivel() {
    let cartasRestantesCount = this.countCartasRestantes()
    return (this._gameOver() || cartasRestantesCount) ? null :
      buttonEmiter(this.props.socket, 'Siguiente nivel', 'subir_nivel')
  }

  renderBotonGameOver() {
    return !this._gameOver() ? null :
      buttonEmiter(this.props.socket, 'GAME OVER', 'juego_quiero_terminar')
  }

  _gameOver() {
    return this.props.vidas !== null && this.props.vidas <= 0
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
      <div
        className="Carta"
        onClick={event => {
          event.preventDefault();
          this.props.socket.emit('poner_carta', {'carta': this.props.valor});
        }}>
        <div className="CartaText">
          {this.props.valor}
        </div>
      </div>
    )
  }
}

function buttonEmiter(socket, button_text, emit_msg) {
  return (
    <button className="CommonButton"
      onClick={event => {
        event.preventDefault();
        socket.emit(emit_msg);
       }}>
      {button_text}
    </button>)
}

export default ManoSection;