
import React, {Component} from 'react'
import Table from './Table'

class App extends Component {
    render() {

        // data
        const characters = [
            {
              name: 'Charlie',
              job:  'Janitor',
            },
            {
              name: 'Mac',
              job:  'Bouncer',
            },
            {
              name: 'Dee',
              job:  'Aspiring actress',
            },
            {
              name: 'Dennis',
              job:  'Bartender',
            },
          ]

        return (
            // pass the data through {characters} to the child (Table) componene 
            <div className="container">
              <Table characterData={characters} />
            </div>
        )
    }
}

export default App