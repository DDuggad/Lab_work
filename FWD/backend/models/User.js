const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  password: {
    type: String,
    required: true,
    minlength: 6
  },
  role: {
    type: String,
    enum: ['Vendor'],
    default: 'Vendor'
  },
  // Restaurant Profile Information
  restaurantName: {
    type: String,
    trim: true
  },
  restaurantImage: {
    type: String,
    trim: true
  },
  location: {
    type: String,
    trim: true
  },
  address: {
    type: String,
    trim: true
  },
  phoneNumber: {
    type: String,
    trim: true
  },
  googleMapsLocation: {
    type: String,
    trim: true
  },
  // Profile completion flag
  profileCompleted: {
    type: Boolean,
    default: false
  },
  // Additional vendor info
  cuisineType: {
    type: String,
    default: 'Pure Veg'
  },
  rating: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true
});

module.exports = mongoose.model('User', userSchema);