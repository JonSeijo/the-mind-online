import React from 'react'

class MesaSection extends React.Component {

  render() {
    return (
      <div>
        <div> Mesa: {this.props.mesa} </div>
      </div>
    )
  }
}

export default MesaSection;