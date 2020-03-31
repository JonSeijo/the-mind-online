import React from 'react'

class IntroView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {value: ''};
  }

  handleChange = (event) => {
    this.setState({value: event.target.value});
  };

  handleSubmit = (event) => {
    this.props.app.setState({view: 'LobbyView'});
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Nombre: <br/>
          <input type="text"
            value={this.state.value}
            onChange={this.handleChange} />
        </label>

        <input type="submit" value="Entrar" />
      </form>
    );
  }
}

export default IntroView;