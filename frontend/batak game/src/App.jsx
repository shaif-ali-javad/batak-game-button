import React, { useState } from 'react';
import './App.css';

import {HashRouter as Router, Routes,Route} from 'react-router-dom';

import Timer from './components/Timer.jsx';
import Userlogin from './components/userlogin.jsx';

function App() {

  return (

      <Router>
        <Routes>
          {/* <Route path='/' element={<Userlogin />} /> */}
          <Route path='/' element={<Timer />} />
        </Routes>
      </Router>
  );
}

export default App;
