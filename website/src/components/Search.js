//todo collect input value from searchBar.js
import React from 'react';

import Searchbar from './Searchbar';

class Search extends React.Component{


    render(){
        // const tag = Object.keys(this.state.tagSementic).map(key => <Searchbar key={key} details={this.state.tagSementic[key]}/>);
        return (
            <div>

                <Searchbar/>
                <section className="bg-dark">
                    <p className="text-cloud"> Vous avez recherchez: {this.props.match.params.tag} <br/>
                        Avec le sentiment: {this.props.match.params.sementic}
                        {/*Todo get the sementic*/}
                    </p>
                </section>

            </div>
        )
    }

}


export default Search;