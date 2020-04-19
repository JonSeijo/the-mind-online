import React from 'react'
import '../css/Juego.css'

class InfoSection extends React.Component {

  render() {
    return (
      <div className="InfoSection">
        <div className="InfoSection_vidas">
          <div> Nivel: {this.props.nivel} </div>
          <div> Vidas: {this.props.vidas} </div>
        </div>

        <div className="InfoSection_cartas">
          <div> Cartas restantes </div>
          <div> {this.renderCantCartasElems()} </div>
        </div>
      </div>
    )
  }

  renderCantCartasElems() {
    if (!this.props.cant_cartas_jugadores) {
      return []
    }

    return Object.entries(this.props.cant_cartas_jugadores)
      .map( ([jug, cant]) =>
        <div key={jug}> {jug + ": " + cant} </div>)
  }

}

export default InfoSection;