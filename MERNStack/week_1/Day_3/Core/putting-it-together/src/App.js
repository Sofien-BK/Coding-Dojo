import './App.css';
import Person_card from './components/Person_card';

function App() {
  const persons = [
    {first_name : "Jane", last_name : "Doe", age : 35, hair_color : "Black" },
    {first_name : "John", last_name : "Smith", age : 88, hair_color : "Brown"},
    {first_name : "Millard", last_name : "Fillmore", age : 50, hair_color : "Brown"},
    {first_name : "Maria", last_name : "Smith", age : 62, hair_color : "Brown"}
  ]


  return (
    <div className="App">
      {persons.map((p) => <Person_card person={p}/>)}
    </div>
  );
}

export default App;

