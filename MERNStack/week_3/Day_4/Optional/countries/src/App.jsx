import { useState } from "react";
import axios from "axios";
import "./App.css";
import Display from "./components/Display";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [countries, setCountries] = useState([]);
  const [newC , setNewC] = useState("")
  const [newF , setNewF] = useState("")
  const fetchCountries = () => {
    axios
      .get("https://restcountries.com/v3.1/all")
      .then((res) => {
        console.log("============>", res.data), setCountries(res.data);
      })
      .catch((err) => console.log("You have an error =====>", err));
  };
  const handleInput = (e) => {
    e.preventDefault();
    setCountries([...countries,{name:{common:newC}, flags : {png:newF}}])
    setNewC("")
    setNewF("")
  }
  const deleteCountry =(id)=> {
    setCountries(countries.filter((c,i) => i !== id ))
  }
  const updateCountry = (id) => {
    const newList = countries
    newList[id].independent = !newList.independent
    setCountries(newList)
  }
  return (
    <>
    <form onSubmit={(e) => {handleInput(e)}}>
    <label >Name</label>
    <input type="text" className="form-control" value={newC} onChange={(e)=>{setNewC(e.target.value)}}/>
    <label >Flag</label>
    <input type="text" className="form-control" value={newF} onChange={(e)=>{setNewF(e.target.value)}}/>
    <button>ADD</button>
    </form>
      <button onClick={fetchCountries}>Fetch Countries</button>
      <table>
        <tr>
          <th>Country Name</th>
          <th>Flag</th>
          <th>Actions</th>
        </tr>
        {countries.map((country, idx) => {
          return <Display country={country} idx={idx} deleteCountry = {deleteCountry}/>;
        })}
      </table>
    </>
  );
}

export default App;
