import React from 'react'
import './SectionStyles.css'

class InfoSection extends React.Component {

  render() {
    let cantCartasElems = this.buildCantCartasElems()
    return (
      <div className="InfoSection">
        <div> Nivel: {this.props.nivel} </div>
        <div> Vidas: {this.props.vidas} </div>
        <div> Cartas restantes: {cantCartasElems} </div>
      </div>
    )
  }

  buildCantCartasElems() {
    if (!this.props.cant_cartas_jugadores) {
      return []
    }

    return Object.entries(this.props.cant_cartas_jugadores)
      .map( ([jug, cant]) =>
        <li key={jug}> {jug + ": " + cant} </li>)
  }

}

export default InfoSection;