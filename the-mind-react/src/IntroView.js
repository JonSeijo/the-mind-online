import React from 'react'
import './css/Common.css'
import './css/Intro.css'

class IntroView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      player_name: '',
      lobby_name: ''
    };
  }

  handlePlayerNameChange(event) {
    let name = event.target.value
    if (this.isValidName(name)) {
      this.setState({player_name: name});
    }
  }

  handleLobbyNameChange(event) {
    let name = event.target.value
    if (this.isValidName(name)) {
      this.setState({lobby_name: name});
    }
  }

  handleSubmit(event) {
    event.preventDefault();
    let player_name = this.state.player_name;
    let lobby_name = this.state.lobby_name;

    if (player_name && lobby_name) {
      this.props.socket.emit(
      'lobby_agregar_jugador', {
        'player_name': player_name,
        'lobby_name': lobby_name,
      })

      this.props.app.setState({
        view: 'LobbyView',
        player_name: player_name,
        lobby_name: lobby_name
      });
    }
  }

  render() {
    return (
      <div className="IntroWrapper">

        <div className="IntroTitle">The Mind</div>

        <div className="IntroContent">
          <form onSubmit={event => this.handleSubmit(event)}>

            <div className="IntroInputContainter">
              <div className="IntroInputTitle"> Nombre </div>
              <input className="IntroInputTextBox"
                type="text"
                value={this.state.player_name}
                onChange={event => this.handlePlayerNameChange(event)} />
            </div>

            <div className="IntroInputContainter">
              <div className="IntroInputTitle"> Lobby </div>
              <input className="IntroInputTextBox"
                type="text"
                value={this.state.lobby_name}
                onChange={event => this.handleLobbyNameChange(event)} />
            </div>

            <input className="CommonButton"
              type="submit" value="Entrar" />

          </form>
        </div>
      </div>
    );
  }

  isValidName(name) {
    return name.length < 22
  }

}

export default IntroView;