const mongoose = require('mongoose');

const dealSchema = new mongoose.Schema({
  vendorId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
    index: true
  },
  itemName: {
    type: String,
    required: [true, 'Item name is required'],
    trim: true,
    maxlength: [100, 'Item name cannot exceed 100 characters']
  },
  description: {
    type: String,
    trim: true,
    maxlength: [500, 'Description cannot exceed 500 characters']
  },
  originalPrice: {
    type: Number,
    required: [true, 'Original price is required'],
    min: [0, 'Original price cannot be negative']
  },
  newPrice: {
    type: Number,
    required: [true, 'New price is required'],
    min: [0, 'New price cannot be negative']
  },
  currency: {
    type: String,
    default: 'INR',
    enum: ['INR']
  },
  stockAvailable: {
    type: Number,
    required: [true, 'Stock is required'],
    min: [0, 'Stock cannot be negative']
  },
  claimed: {
    type: Number,
    default: 0,
    min: [0, 'Claimed cannot be negative']
  },
  dealStartTime: {
    type: Date,
    required: [true, 'Deal start time is required'],
    index: true
  },
  dealEndTime: {
    type: Date,
    required: [true, 'Deal end time is required']
  },
  image: {
    type: String,
    trim: true
  },
  foodType: {
    type: String,
    required: [true, 'Food type is required'],
    enum: ['South Indian', 'North Indian', 'Italian', 'Chinese', 'Continental', 'Multi-Cuisine', 'Pure Veg'],
    index: true
  },
  isActive: {
    type: Boolean,
    default: true,
    index: true
  },
  vendor: {
    restaurantName: { type: String, required: true, trim: true },
    address: { type: String, required: true, trim: true },
    location: { type: String, required: true, trim: true, index: true },
    phoneNumber: { type: String, required: true, trim: true },
    googleMapsLocation: { type: String, trim: true },
    rating: { type: Number, min: 0, max: 5, default: 0 }
  }
}, { timestamps: true });

dealSchema.index({ 'vendor.location': 1, foodType: 1 });
dealSchema.index({ dealStartTime: 1, dealEndTime: 1 });
dealSchema.index({ isActive: 1, createdAt: -1 });

dealSchema.virtual('availableStock').get(function() {
  return this.stockAvailable - this.claimed;
});

dealSchema.virtual('discountPercentage').get(function() {
  if (this.originalPrice <= 0) return 0;
  return Math.round(((this.originalPrice - this.newPrice) / this.originalPrice) * 100);
});

dealSchema.pre('save', function(next) {
  if (this.dealEndTime <= this.dealStartTime) {
    return next(new Error('Deal end time must be after start time'));
  }
  if (this.newPrice >= this.originalPrice) {
    return next(new Error('New price must be less than original price'));
  }
  next();
});

dealSchema.set('toJSON', { virtuals: true });
dealSchema.set('toObject', { virtuals: true });

module.exports = mongoose.model('Deal', dealSchema);
