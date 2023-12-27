import React from 'react'

const Person_card = ({person}) => {
    const {first_name , last_name , age , hair_color} = person;
  return (
    <div>
      <h1>{last_name} , {first_name}</h1>
      <p>Age : {age}</p>
      <p>Hair Color : {hair_color}</p>
    </div>
  )
}

export default Person_card
