import React, { Component } from 'react';
import * as d3 from 'd3';
import '../style/css/map.css';

class DashBoard extends Component {

    initDashboard(){
         var $ppc = $('.progress-pie-chart'),
        percent = parseInt($ppc.data('percent')),
        deg = 360*percent/100;
      if (percent > 50) {
        $ppc.addClass('gt-50');
      }
      d3.select('.ppc-progress-fill').style('transform','rotate('+ deg +'deg)');
      d3.select('.ppc-percents span').html(percent+'%');

        d3.json("data.json", function(data) {
          console.log(data[0]);
          d3.select('#rt').html(data[0].age)
          d3.select('#like').html(data[0].age)
          d3.select('#man').html(data[0].age)
          d3.select('#woman').html(data[0].age)
    });
    }
  render() {
    return (
           <div class="progressDiv">
            <div class="statChartHolder">
                <div class="progress-pie-chart" data-percent="43"><!--Pie Chart -->
                    <div class="ppc-progress">
                        <div class="ppc-progress-fill"></div>
                    </div>
                    <div class="ppc-percents">
                    <div class="pcc-percents-wrapper">
                        <span>%</span>
                    </div>
                    </div>
                </div><!--End Chart -->
            </div>
            <div class="statRightHolder">


                <ul>
                <li> <h3 id='rt' class="blue"></h3> <span>Retweets</span></li>
                <li> <h3 id='like' class="purple"></h3> <span>Like</span></li>
                </ul>

                    <ul class="statsLeft">
                    <li><h3 id='man'class="yellow"></h3> <span>Homme</span></li>
                    <li><h3 id='woman'class="red"></h3> <span>Femme</span></li>
                    </ul>
                        <ul class="statsRight">
                            <li><h3>18%</h3> <span>Région</span></li>
                            <li><h3>23%</h3> <span>Goals</span></li>
                        </ul>
            </div>

        </div>
    );
  }
}

export default DashBoard;
