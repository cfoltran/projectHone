import React from 'react';

import Searchbar from './Searchbar';
import SearchTweets from './SearchTweets';

export default class Search extends React.Component {
    render() {
        // const tag = Object.keys(this.state.tagSementic).map(key => <Searchbar key={key} details={this.state.tagSementic[key]}/>);
        return (
            <section>
                <div className="searchbar-container">
                    <Searchbar/>
                </div>
                <div>
                    <SearchTweets tag={this.props.match.params.tag} sementic={this.props.match.params.sementic} />
                </div>
            </section>
        );
    }
}