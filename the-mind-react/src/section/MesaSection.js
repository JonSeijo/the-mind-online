import React from 'react'
import './SectionStyles.css'


class MesaSection extends React.Component {

  render() {
    return (
      <div className="MesaSection">
        <div> Mesa: {this.props.mesa} </div>
      </div>
    )
  }
}

export default MesaSection;