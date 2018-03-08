/*
///////////////////////////////////////////////////////////////
                Modal & search bar
///////////////////////////////////////////////////////////////
 */
//React
import React, { Component, PropTypes } from 'react';

//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';


export default class Switch extends Component
{

    constructor(props)
    {
        super(props);
        this.state = {
            clicked: false
        };

    }

    handleSwitch(e)
    {
        this.setState({
            clicked: !this.state.clicked
        });
    }


    render()
    {
        return (
            <div>
                {/*<!--===========================================-->*/}
                {/*          <!-- Switch Day / Night -->             */}
                {/*<!--===========================================-->*/}
                <li>
                    <div class="toggle-mode">
                        <div class="icon">
                            <i class="fa fa-sun-o" aria-hidden="true"></i>
                        </div>
                        <div class="toggle-switch">
                            <label class="switch">
                                <input type="checkbox" id="switch-style" onClick=""/>
                                <div class="slider round"></div>
                            </label>
                        </div>
                        <div class="icon">
                            <i class="fa fa-moon-o" aria-hidden="true"></i>
                        </div>
                    </div>
                </li>
            </div>
        );
    }
}
