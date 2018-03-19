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
            var $ppc = d3.select('.progress-pie-chart'),
            percent = parseInt($ppc.data('percent')),
            deg = 360*percent/100;
          if (percent > 50) {
            $ppc.addClass('gt-50');
          }
          d3.select('.ppc-progress-fill').style('transform','rotate('+ deg +'deg)');
          d3.select('.ppc-percents span').html(percent+'%');

            d3.json("/static/dataForDashBoard.json", function(data) {
              console.log(data[0]);
              d3.select('#rt').html(data[0].age);
              d3.select('#like').html(data[0].age);
              d3.select('#man').html(data[0].age);
              d3.select('#woman').html(data[0].age)
        });
    }
  render() {
    return (
           <div className="progressDiv">
            <div className="statChartHolder">
                {/*Pie Chart*/}
                <div className="progress-pie-chart" data-percent="43">
                    <div className="ppc-progress">
                        <div className="ppc-progress-fill"></div>
                    </div>
                    <div className="ppc-percents">
                    <div className="pcc-percents-wrapper">
                        <span>%</span>
                    </div>
                    </div>
                </div>
                {/*End Chart*/}
            </div>
            <div className="statRightHolder">


                <ul>
                <li> <h3 id='rt' className="blue"></h3> <span>Retweets</span></li>
                <li> <h3 id='like' className="purple"></h3> <span>Like</span></li>
                </ul>

                    <ul className="statsLeft">
                    <li><h3 id='man'className="yellow"></h3> <span>Homme</span></li>
                    <li><h3 id='woman'className="red"></h3> <span>Femme</span></li>
                    </ul>
                        <ul className="statsRight">
                            <li><h3>18%</h3> <span>Région</span></li>
                            <li><h3>23%</h3> <span>Goals</span></li>
                        </ul>
            </div>

        </div>
    );
  }
}

export default DashBoard;