import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import NumberPage from './components/NumberPage';
import WordPage from './components/WordPage';
import StyleWordPage from './components/StyleWordPage';
import NotFound from './components/NotFound';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/home" component={Home} />
        <Route path="/:number" component={NumberPage} />
        <Route path="/hello" exact component={WordPage} />
        <Route path="/hello/:text" exact component={WordPage} />
        <Route path="/hello/:text/:color/:background" component={StyleWordPage} />
        <Route component={NotFound} />
      </Switch>
    </Router>
  );
}

export default App;