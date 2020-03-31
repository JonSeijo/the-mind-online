import React from 'react'

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
      this.props.app.setState({
        view: 'LobbyView',
        name: name
      });
    }
  }

  render() {
    return (
      <form onSubmit={event => this.handleSubmit(event)}>
        <label>
          Nombre: <br/>
          <input type="text"
            value={this.state.name}
            onChange={event => this.handleChange(event)} />
        </label>

        <input type="submit" value="Entrar" />
      </form>
    );
  }
}

export default IntroView;