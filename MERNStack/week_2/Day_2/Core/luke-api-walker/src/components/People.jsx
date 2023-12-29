import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const PeopleDetails = () => {
  const { id } = useParams();
  const [person, setPerson] = useState({});
  const [homeworld, setHomeworld] = useState('');

  useEffect(() => {
    axios.get(`https://swapi.dev/api/people/${id}`)
      .then((response) => {
        setPerson(response.data);
        return axios.get(response.data.homeworld);
      })
      .then((homeworldResponse) => {
        setHomeworld(homeworldResponse.data.name);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, [id]);

  return (
    <div>
      <h2>{person.name}</h2>
      <p>Height: {person.height}</p>
      <p>Mass: {person.mass}</p>
      <p>Homeworld: {homeworld}</p>
    </div>
  );
};

export default PeopleDetails;
