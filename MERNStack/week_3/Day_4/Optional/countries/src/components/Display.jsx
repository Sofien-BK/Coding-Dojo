import React, { useState } from "react";

const Display = ({ country, idx }) => {
  const [thisCountry, setThisCountry] = useState(country);
  return (
    <div>
        <tr>
          <td>{thisCountry.name.common}</td>
          <td>
            <img src={thisCountry.flags.png} />
          </td>
          <td>
            <input type="checkbox" /> Independent | <button onClick={(e) =>{props.deleteCountry(props.idx)}}>Delete</button>
          </td>
        </tr>
    </div>
  );
};

export default Display;
