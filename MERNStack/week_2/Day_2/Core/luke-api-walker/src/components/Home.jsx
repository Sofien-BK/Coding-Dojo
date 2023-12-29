import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const Home = () => {
  const [resource, setResource] = useState('people');
  const [id, setId] = useState('');
  const history = useHistory();

  const handleResourceChange = (e) => {
    setResource(e.target.value);
  };

  const handleIdChange = (e) => {
    setId(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    history.push(`/${resource}/${id}`);
  };

  return (
    <div>
      <h2>Welcome to the Star Wars API Explorer!</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Choose a resource:
          <select value={resource} onChange={handleResourceChange}>
            <option value="people">People</option>
            <option value="planets">Planets</option>
          </select>
        </label>
        <label>
          Enter ID:
          <input type="text" value={id} onChange={handleIdChange} />
        </label>
        <button type="submit">Fetch Details</button>
      </form>
    </div>
  );
};

export default Home;
