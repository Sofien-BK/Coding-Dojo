import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const PlanetDetails = () => {
  const { id } = useParams();
  const [planet, setPlanet] = useState({});

  useEffect(() => {
    axios.get(`https://swapi.dev/api/planets/${id}`)
      .then((response) => {
        setPlanet(response.data);
      })
      .catch((error) => {
        console.error('Error fetching planet details:', error);
      });
  }, [id]);

  return (
    <div>
      <h2>{planet.name}</h2>
      <p>Population: {planet.population}</p>
      <p>Climate: {planet.climate}</p>
    </div>
  );
};

export default PlanetDetails;
