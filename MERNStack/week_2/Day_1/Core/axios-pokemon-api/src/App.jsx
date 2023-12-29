import React from 'react';
import './App.css'; 
import PokemonFetcher from './components/Pokemon'; 

function App() {
  return (
    <div className="App">
      <h1>Pokemon API Fetcher 🐾</h1>
      <PokemonFetcher />
    </div>
  );
}

export default App;
