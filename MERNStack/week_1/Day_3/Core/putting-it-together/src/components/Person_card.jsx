import React , {useState} from 'react'

const Person_card = ({person}) => {
    const {first_name , last_name , hair_color} = person;
    const [age , setAge] = useState(person.age);
    const birthday = () => {
        setAge(age + 1)
    }
  return (
    <div>
      <h1>{last_name} , {first_name}</h1>
      <p>Age : {age}</p>
      <p>Hair Color : {hair_color}</p>
      <button onClick={birthday}>Birthday Button For {first_name} {last_name}</button>
    </div>
  )
}

export default Person_card
