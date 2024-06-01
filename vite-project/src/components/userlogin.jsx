import React, { useState } from 'react';

import axios from 'axios';

function App() {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:3000/register', { name })
      .then(result => { console.log(result) 
        navigation("#/timer")
      })
      .catch(error => { console.error(error) });
  };

  const handleChange = (e) => {
    setName(e.target.value);
  };

  const goFullScreen = () => {
    window.electron.setFullScreen(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Batak game</h1>
        <form onSubmit={handleSubmit}>
          <input type="text" value={name} onChange={handleChange} /><br />
          <button type='submit' onClick={goFullScreen}>Login</button>
        </form>
      </header>
    </div>
  );
}

export default App;
