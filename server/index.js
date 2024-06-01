const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const { User } = require('./models/user');

const app = express()
app.use(express.json())
app.use(cors())

mongoose.connect('mongodb://localhost:27017/batak')

app.post('/register', (req, res) => {
    User.create(req.body)
    .then((user) => res.json(user))
    .catch((err) => res.json(err))    
    })

app.get('/getuser', (req, res) => {
    User.find().then((user) => res.json(user))
    .catch((err) => res.json(err))
    })

    app.listen(3000, () => {
        console.log('Server is running on port 3000')
    })