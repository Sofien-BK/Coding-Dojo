import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import PeopleDetails from './components/People';
import PlanetDetails from './components/Planet';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/people/:id" component={PeopleDetails} /> 
        <Route path="/planets/:id" component={PlanetDetails} />
      </Switch>
    </Router>
  );
}

export default App;
