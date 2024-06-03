const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const { User } = require('./models/user');

const app = express()
app.use(express.json())
app.use(cors())

mongoose.connect('mongodb://localhost:27017/batak')

app.post('/register', (req, res) => {
    const { name, timerData } = req.body; // Destructure name and timerData from the request body
    User.create({ name, timerData }) // Create a new user document with name and timerData
        .then((user) => res.json(user))
        .catch((err) => res.json(err));    
});

  

app.get('/getuser', (req, res) => {
    User.find().then((user) => res.json(user))
    .catch((err) => res.json(err))
    })

    app.listen(3000, () => {
        console.log('Server is running on port 3000')
    })