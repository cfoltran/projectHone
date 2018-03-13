import React, { Component } from 'react';
import * as d3 from 'd3';
import DashBoard from "./DashBoard";
import '../style/css/map.css';

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
