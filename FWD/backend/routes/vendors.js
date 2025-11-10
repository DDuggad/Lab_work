const express = require('express');
const User = require('../models/User');

const router = express.Router();

// Get all vendors
router.get('/', async (req, res) => {
  try {
    const vendors = await User.find({ role: 'Vendor' }).select('-password');
    res.json(vendors);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Server error' });
  }
});

// Get vendor by ID
router.get('/:id', async (req, res) => {
  try {
    const vendor = await User.findOne({ 
      _id: req.params.id, 
      role: 'Vendor' 
    }).select('-password');
    
    if (!vendor) {
      return res.status(404).json({ message: 'Vendor not found' });
    }
    
    res.json(vendor);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Server error' });
  }
});

// Update vendor profile
router.put('/:id', async (req, res) => {
  try {
    const { vendorProfile } = req.body;
    
    const vendor = await User.findOneAndUpdate(
      { _id: req.params.id, role: 'Vendor' },
      { vendorProfile },
      { new: true }
    ).select('-password');
    
    if (!vendor) {
      return res.status(404).json({ message: 'Vendor not found' });
    }
    
    res.json({
      message: 'Vendor profile updated successfully',
      vendor
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Server error' });
  }
});

module.exports = router;