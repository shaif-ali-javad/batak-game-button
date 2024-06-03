const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userSchema = new Schema({
    name: String,
    timerData: String // Add a field for timer data
});

const User = mongoose.model('User', userSchema);

module.exports = {
  User: User
};
