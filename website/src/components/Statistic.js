import React, { Component } from 'react';
import DashBoard from "./DashBoard";
import '../style/scss/style.css';

class Statistic extends Component {
  render() {
    return (
        <section>
            <div>
                <DashBoard/>
            </div>
        </section>
    );
  }
}

export default Statistic;
