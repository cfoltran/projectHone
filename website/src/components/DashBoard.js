import React, { Component } from 'react';
import * as d3 from 'd3';
import '../style/css/DashBoard.css';

class DashBoard extends Component {

    componentDidMount() {
        this.initDashboard()
    }

    componentDidUpdate(){
        this.initDashboard()
    }

    initDashboard(){
            var ppc = d3.select('.progress-pie-chart'),
            percent = parseInt(ppc.data('percent'),10),
            deg = 360*percent/100;
          if (percent > 50) {
            ppc.addClass('gt-50');
          }
          d3.select('.ppc-progress-fill').style('transform','rotate('+ deg +'deg)');
          d3.select('.ppc-percents span').html(percent+'%');

            d3.json("/static/dataForDashBoard.json", function(data) {
              console.log(data[0]);
              d3.select('#tweet').html(data[0].age);
              d3.select('#rt').html(data[1].age);
 				d3.select('#humeur').html(data[1].age);
            
        });
    }
  render() {
    return (
           <div className="progressDiv">
            <div className="statChartHolder">
                {/*Pie Chart*/}
                <div className="progress-pie-chart" data-percent="90">
                    <div className="ppc-progress">
                        <div className="ppc-progress-fill"></div>
                    </div>
                    <div className="ppc-percents">
                    <div className="pcc-percents-wrapper">
                        <span> 4%</span>
                    </div>
                    </div>
                </div>
                {/*End Chart*/}
            </div>
            <div className="statRightHolder">

                <ul>
                    <li> <h3><span>Nombre de Tweet</span></h3> <div id='tweet' className="font-30"/>
                  </li>
                    <li> <h3><span>Nombre de RT moyen</span></h3> <div id='rt' className="font-30"/> </li>
					<li> <h3><span>Humeur</span></h3> <div id='humeur' className="font-30"/> </li>
                </ul>

                    
            </div>

        </div>
    );
  }
}

export default DashBoard;

