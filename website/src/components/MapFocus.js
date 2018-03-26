import React, { Component } from 'react';

class MapFocus extends Component {
    
    constructor (props) {
        super(props);
    }

    render() {
        return (<p> { this.props.match.params.region}</p>)
    }
}

export default MapFocus