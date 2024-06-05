import React, { useState } from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import { Button } from "@mui/material";

function App() {
  const [name, setName] = useState('');

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   axios.post('http://localhost:3000/register', { name }) // Include the time field
  //     .then(result => { console.log(result); })
  //     .catch(error => { console.error(error); });
  // };
  

  const handleChange = (e) => {
    setName(e.target.value);
  };

  const goFullScreen = () => {
    if (window.electron && window.electron.setFullScreen) {
      window.electron.setFullScreen(true);
    } else {
      console.error('Electron API not available');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Batak game</h1>
        <form >
          <input type="text" value={name} onChange={handleChange} /><br />
          <NavLink to="/timer">
            <Button type='submit' onClick={goFullScreen}>Login</Button>
          </NavLink>
        </form>
      </header>
    </div>
  );
}

export default App;
