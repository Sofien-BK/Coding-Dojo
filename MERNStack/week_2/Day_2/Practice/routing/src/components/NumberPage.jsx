import React from 'react';
import { useParams } from 'react-router-dom';

const NumberPage = () => {
  const { number } = useParams();
  return <h2>{number}</h2>;
};

export default NumberPage;
