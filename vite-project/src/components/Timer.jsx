  import React, { useEffect, useState } from 'react';
  import { Button, Typography } from '@mui/material';
  import './timer.css';

  import axios from 'axios';

  function App() {
    const [minutes, setMinutes] = useState(0);
    const [seconds, setSeconds] = useState(0);
    const [timerRunning, setTimerRunning] = useState(true); // State to track if the timer is running
    const [name, setName] = useState('');

    // Set a future deadline
    const duration = 60; // 5 seconds
    const deadline = new Date();
    deadline.setSeconds(deadline.getSeconds() + duration);

    const getTime = () => {
      const currentTime = new Date();
      const timeDifference = deadline - currentTime;

      if (timeDifference <= 0) {
        clearInterval(intervalRef.current); // Stop the interval when time reaches zero
        setTimerRunning(false);
        setMinutes(0);
        setSeconds(0);
      } else {
        setMinutes(Math.floor((timeDifference / 1000 / 60) % 60));
        setSeconds(Math.floor((timeDifference / 1000) % 60));
      }
    };

    const intervalRef = React.useRef(null); // Ref to hold interval ID

    useEffect(() => {
      intervalRef.current = setInterval(getTime, 1000); // Start the timer interval
      getTime(); // Initial call to update timer display immediately

      return () => clearInterval(intervalRef.current); // Cleanup function to clear the interval
    }, []);

    const start = () => {
      clearInterval(intervalRef.current); // Stop the timer interval
      setTimerRunning(true);
    };
    const stop = () => {
      clearInterval(intervalRef.current); // Stop the timer interval
      setTimerRunning(false);
    };

    const handleSubmit = (e) => {
      e.preventDefault();
      const currentTime = `${minutes}:${seconds < 10 ? "0" + seconds : seconds}`; // Combine minutes and seconds
      axios.post('http://localhost:3000/register', { name, timerData: currentTime }) // Include both name and timerData
        .then(result => { console.log(result); })
        .catch(error => { console.error(error); });
    };        
    

    const handleChange = (e) => {
      setName(e.target.value);
    };

    return (
      <div className="App">
        <Typography variant='h1' className="title">Batak Game</Typography>
        <header className="timer-header">
          <Typography variant='h2' className="subtitle">Timer</Typography>
          <input type="text" value={name} onChange={handleChange} /><br />
          <Typography variant="h3" className="timer">
            {seconds < 10 ? "0" + seconds : seconds}
          </Typography>
          <Button variant="contained" color="primary" onClick={start} disabled={timerRunning}>Start</Button>
          <Button variant="contained" color="primary" onClick={stop} disabled={!timerRunning}>Stop</Button>
          <Button variant='contained' color='primary' onClick={handleSubmit}>Submit</Button>
        </header>
      </div>
    );
  }

  export default App;
