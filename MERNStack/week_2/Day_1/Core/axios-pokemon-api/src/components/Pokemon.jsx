import React, { useState } from 'react';
import axios from 'axios';

const PokemonFetcher = () => {
  const [pokemonList, setPokemonList] = useState([]);

  const fetchPokemon = () => {
    axios.get('https://pokeapi.co/api/v2/pokemon?limit=807')
      .then((response) => {
        const { results } = response.data;
        const names = results.map((pokemon) => pokemon.name);
        setPokemonList(names);
      })
      .catch((error) => {
        console.error('Error fetching Pokemon:', error);
      });
  };

  return (
    <div>
      <h1>Pokemon List</h1>
      <button onClick={fetchPokemon}>Fetch Pokemon</button>
      <ul>
        {pokemonList.map((pokemon, index) => (
          <li key={index}>{pokemon}</li>
        ))}
      </ul>
    </div>
  );
};

export default PokemonFetcher;
