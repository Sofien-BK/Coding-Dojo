import React from 'react';
import { useParams } from 'react-router-dom';

const StyleWordPage = () => {
  const { text, color, background } = useParams();
  const styles = {
    color: color || 'black',
    backgroundColor: background || 'white',
  };
  return <h2 style={styles}>{text}</h2>;
};

export default StyleWordPage;