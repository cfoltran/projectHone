/*
///////////////////////////////////////////////////////////////
                Modal & search bar
///////////////////////////////////////////////////////////////
 */
//React
import React, { Component } from 'react';

//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';


export default class Switch extends Component
{


    toggle = event => {
        this.props.onSwitchHome(!this.props.checked);
    };
    

    render()
    {
        return (
            <div className="font-40">
                {/*<!--===========================================-->*/}
                {/*          <!-- Switch Day / Night -->             */}
                {/*<!--===========================================-->*/}
                    <div className="toggle-mode">
                        <div className="icon">
                            <i className="fa fa-sun-o " aria-hidden="true"/>
                        </div>
                        <div className="toggle-switch">
                            <label className="switch">
                                <input type="checkbox" checked={this.props.checked} onChange={e => this.toggle(e)} id="switch-style"/>

                                <div className="slider round"/>
                            </label>
                        </div>
                        <div className="icon">
                            <i className="fa fa-moon-o " aria-hidden="true"/>
                        </div>
                    </div>
            </div>
        );
    }
}
