import React from 'react';
import { useParams } from 'react-router-dom';

const WordPage = () => {
  const { text } = useParams();
  return <h2>{text}</h2>;
};

export default WordPage;
