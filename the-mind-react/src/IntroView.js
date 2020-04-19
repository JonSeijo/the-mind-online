import React from 'react'
import './css/Intro.css'

class IntroView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {name: ''};
  }

  handleChange(event) {
    this.setState({name: event.target.value});
  };

  handleSubmit(event) {
    event.preventDefault();
    let name = this.state.name;

    if (name) {
      this.props.socket.emit(
      'lobby_agregar_jugador', {
        'name': name
      })

      this.props.app.setState({
        view: 'LobbyView',
        name: name
      });
    }
  }

  render() {
    return (
      <div className="IntroWrapper">

        <div className="IntroTitle">The Mind</div>

        <div className="IntroContent">
          <form onSubmit={event => this.handleSubmit(event)}>
            <div className="IntroInputTitle">
              Nombre
            </div>

            <input type="text"
              value={this.state.name}
              onChange={event => this.handleChange(event)} />
            <input type="submit" value="Entrar" />
          </form>
        </div>
      </div>
    );
  }
}

export default IntroView;