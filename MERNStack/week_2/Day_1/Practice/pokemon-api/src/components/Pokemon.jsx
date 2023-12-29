import React, { useState } from 'react';
import axios from 'axios';

const Pokemon = () => {
  const [pokemonList, setPokemonList] = useState([]);

  const fetchPokemon = async () => {
    try {
      const response = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=807');
      const { results } = response.data;
      setPokemonList(results.map((pokemon) => pokemon.name));
    } catch (error) {
      console.error('Error fetching Pokemon:', error);
    }
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

export default Pokemon;
