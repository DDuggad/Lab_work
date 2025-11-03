const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const dotenv = require('dotenv');
const User = require('./models/User');
const Deal = require('./models/Deal');

dotenv.config();

// Connect to MongoDB
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/freshbites');
    console.log('✅ MongoDB Connected for seeding');
  } catch (error) {
    console.error('❌ MongoDB connection error:', error);
    process.exit(1);
  }
};

// Sample vendor accounts with real Bangalore Pure Veg restaurant data
const vendors = [
  {
    username: 'mtr_basavanagudi',
    email: 'mtr@freshbites.com',
    password: 'vendor123',
    restaurantName: 'MTR (Mavalli Tiffin Room)',
    location: 'Basavanagudi',
    address: '11, Lalbagh Road, Basavanagudi, Bangalore - 560004',
    phoneNumber: '9876543201',
    restaurantImage: 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=MTR+Basavanagudi+Bangalore',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'vidyarthi_bhavan',
    email: 'vidyarthi@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Vidyarthi Bhavan',
    location: 'Basavanagudi',
    address: '32, Gandhi Bazaar Main Road, Basavanagudi, Bangalore - 560004',
    phoneNumber: '9876543202',
    restaurantImage: 'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Vidyarthi+Bhavan+Bangalore',
    profileCompleted: true,
    cuisineType: 'South Indian'
  },
  {
    username: 'brahmin_thatte_idli',
    email: 'brahmin@freshbites.com',
    password: 'vendor123',
    restaurantName: "Brahmins' Thatte Idli",
    location: 'Jayanagar',
    address: '426, 11th Main Road, 4th Block, Jayanagar, Bangalore - 560011',
    phoneNumber: '9876543203',
    restaurantImage: 'https://images.unsplash.com/photo-1630383249896-424e482df921?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Brahmin+Thatte+Idli+Jayanagar',
    profileCompleted: true,
    cuisineType: 'South Indian'
  },
  {
    username: 'maiyas_restaurant',
    email: 'maiyas@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Maiyas Restaurant',
    location: 'Jayanagar',
    address: '146, 3rd Block, Jayanagar, Bangalore - 560011',
    phoneNumber: '9876543204',
    restaurantImage: 'https://images.unsplash.com/photo-1546833998-877b37c2e5c6?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Maiyas+Jayanagar+Bangalore',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'upahara_darshini',
    email: 'upahara@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Upahara Darshini',
    location: 'Jayanagar',
    address: '18th Cross, 3rd Block, Jayanagar, Bangalore - 560011',
    phoneNumber: '9876543205',
    restaurantImage: 'https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Upahara+Darshini+Jayanagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'vegarama_rajajinagar',
    email: 'vegarama@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Vegarama',
    location: 'Rajajinagar',
    address: '45, 10th Main Road, Rajajinagar, Bangalore - 560010',
    phoneNumber: '9876543206',
    restaurantImage: 'https://images.unsplash.com/photo-1606787366850-de6330128bfc?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Vegarama+Rajajinagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'nandhini_deluxe',
    email: 'nandhini@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Nandhini Deluxe',
    location: 'Rajajinagar',
    address: '69, Chord Road, Rajajinagar, Bangalore - 560010',
    phoneNumber: '9876543207',
    restaurantImage: 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Nandhini+Deluxe+Rajajinagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'sagar_ratna',
    email: 'sagar@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Sagar Ratna',
    location: 'Rajajinagar',
    address: '25, 8th Main Road, Rajajinagar, Bangalore - 560010',
    phoneNumber: '9876543208',
    restaurantImage: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Sagar+Ratna+Rajajinagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'sri_sagar_hn',
    email: 'srisagar@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Sri Sagar (CTR)',
    location: 'Hanumanth Nagar',
    address: '52, Ring Road, Hanumanth Nagar, Bangalore - 560019',
    phoneNumber: '9876543209',
    restaurantImage: 'https://images.unsplash.com/photo-1623428187969-5da2dcea5ebf?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Sri+Sagar+Hanumanth+Nagar',
    profileCompleted: true,
    cuisineType: 'South Indian'
  },
  {
    username: 'veg_palace_hn',
    email: 'vegpalace@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Veg Palace',
    location: 'Hanumanth Nagar',
    address: '78, 1st Main Road, Hanumanth Nagar, Bangalore - 560019',
    phoneNumber: '9876543210',
    restaurantImage: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Veg+Palace+Hanumanth+Nagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'rameshwaram_cafe',
    email: 'rameshwaram@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Rameshwaram Cafe',
    location: 'Malleshwaram',
    address: '35, Sampige Road, Malleshwaram, Bangalore - 560003',
    phoneNumber: '9876543211',
    restaurantImage: 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Rameshwaram+Cafe+Malleshwaram',
    profileCompleted: true,
    cuisineType: 'South Indian'
  },
  {
    username: 'ctr_malleshwaram',
    email: 'ctr@freshbites.com',
    password: 'vendor123',
    restaurantName: 'CTR (Central Tiffin Room)',
    location: 'Malleshwaram',
    address: '56, Margosa Road, Malleshwaram, Bangalore - 560003',
    phoneNumber: '9876543212',
    restaurantImage: 'https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=CTR+Malleshwaram+Bangalore',
    profileCompleted: true,
    cuisineType: 'South Indian'
  },
  {
    username: 'kamat_hotel',
    email: 'kamat@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Kamat Hotel',
    location: 'Malleshwaram',
    address: '12, 8th Cross, Malleshwaram, Bangalore - 560003',
    phoneNumber: '9876543213',
    restaurantImage: 'https://images.unsplash.com/photo-1606787366850-de6330128bfc?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Kamat+Hotel+Malleshwaram',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'rasovara_indiranagar',
    email: 'rasovara@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Rasovara',
    location: 'Indiranagar',
    address: '234, 100 Feet Road, Indiranagar, Bangalore - 560038',
    phoneNumber: '9876543214',
    restaurantImage: 'https://images.unsplash.com/photo-1544025162-d76694265947?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Rasovara+Indiranagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'green_theory_indiranagar',
    email: 'greentheory@freshbites.com',
    password: 'vendor123',
    restaurantName: 'The Green Theory',
    location: 'Indiranagar',
    address: '45, 12th Main Road, Indiranagar, Bangalore - 560038',
    phoneNumber: '9876543215',
    restaurantImage: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Green+Theory+Indiranagar',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'green_thaali_koramangala',
    email: 'greenthaali@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Green Thaali',
    location: 'Koramangala',
    address: '78, 5th Block, Koramangala, Bangalore - 560095',
    phoneNumber: '9876543216',
    restaurantImage: 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Green+Thaali+Koramangala',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  },
  {
    username: 'onesta_koramangala',
    email: 'onesta@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Onesta (Veg)',
    location: 'Koramangala',
    address: '156, 7th Block, Koramangala, Bangalore - 560095',
    phoneNumber: '9876543217',
    restaurantImage: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Onesta+Koramangala',
    profileCompleted: true,
    cuisineType: 'Multi-Cuisine'
  },
  {
    username: 'pureveg_btm',
    email: 'pureveg@freshbites.com',
    password: 'vendor123',
    restaurantName: 'Pure Veg Restaurant',
    location: 'BTM Layout',
    address: '45, 14th Main, BTM Layout 2nd Stage, Bangalore - 560076',
    phoneNumber: '9876543218',
    restaurantImage: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400',
    googleMapsLocation: 'https://maps.google.com/?q=Pure+Veg+BTM+Layout',
    profileCompleted: true,
    cuisineType: 'Pure Veg'
  }
];

// Function to create deals for a vendor
const createDealsForVendor = (vendor) => {
  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  
  // Helper to create time slots
  const getTimeSlot = (startHour, endHour, daysOffset = 0) => {
    const start = new Date(today);
    start.setDate(start.getDate() + daysOffset);
    start.setHours(startHour, 0, 0, 0);
    
    const end = new Date(today);
    end.setDate(end.getDate() + daysOffset);
    end.setHours(endHour, 0, 0, 0);
    
    return { start, end };
  };

  const dealTemplates = {
    'MTR (Mavalli Tiffin Room)': [
      { item: 'Rava Idli Combo', original: 120, new: 80, stock: 30, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Masala Dosa Set', original: 150, new: 100, stock: 25, type: 'South Indian', slot: getTimeSlot(18, 20) }
    ],
    'Vidyarthi Bhavan': [
      { item: 'Benne Masala Dosa', original: 85, new: 60, stock: 40, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Set Dosa with Chutney', original: 70, new: 50, stock: 35, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    "Brahmins' Thatte Idli": [
      { item: 'Thatte Idli (3 pcs)', original: 60, new: 40, stock: 50, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Idli Vada Combo', original: 80, new: 55, stock: 40, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'Maiyas Restaurant': [
      { item: 'Veg Thali', original: 200, new: 140, stock: 20, type: 'Pure Veg', slot: getTimeSlot(18, 20) },
      { item: 'North Indian Meal', original: 180, new: 130, stock: 25, type: 'North Indian', slot: getTimeSlot(19, 21) }
    ],
    'Upahara Darshini': [
      { item: 'Pongal Special', original: 65, new: 45, stock: 35, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Mini Meals', original: 90, new: 65, stock: 30, type: 'Pure Veg', slot: getTimeSlot(18, 20) }
    ],
    'Vegarama': [
      { item: 'Paneer Butter Masala Meal', original: 180, new: 130, stock: 25, type: 'North Indian', slot: getTimeSlot(18, 20) },
      { item: 'South Indian Thali', original: 150, new: 110, stock: 30, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'Nandhini Deluxe': [
      { item: 'Veg Pulao Combo', original: 140, new: 100, stock: 28, type: 'Pure Veg', slot: getTimeSlot(18, 20) },
      { item: 'Paneer Fried Rice', original: 160, new: 115, stock: 25, type: 'Chinese', slot: getTimeSlot(19, 21) }
    ],
    'Sagar Ratna': [
      { item: 'Paper Roast Dosa', original: 95, new: 70, stock: 35, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Mini Uttapam Set', original: 85, new: 60, stock: 30, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'Sri Sagar (CTR)': [
      { item: 'Filter Coffee + Vada', original: 50, new: 35, stock: 45, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Bisibelebath', original: 75, new: 55, stock: 35, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'Veg Palace': [
      { item: 'Chinese Combo', original: 170, new: 120, stock: 22, type: 'Chinese', slot: getTimeSlot(18, 20) },
      { item: 'Veg Manchurian Meal', original: 150, new: 110, stock: 25, type: 'Chinese', slot: getTimeSlot(19, 21) }
    ],
    'Rameshwaram Cafe': [
      { item: 'Ghee Podi Dosa', original: 100, new: 70, stock: 40, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Filter Coffee + Snacks', original: 60, new: 45, stock: 50, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'CTR (Central Tiffin Room)': [
      { item: 'Benne Dose', original: 80, new: 60, stock: 38, type: 'South Indian', slot: getTimeSlot(16, 18) },
      { item: 'Khara Bath', original: 65, new: 48, stock: 35, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'Kamat Hotel': [
      { item: 'Veg Meals', original: 130, new: 95, stock: 30, type: 'Pure Veg', slot: getTimeSlot(18, 20) },
      { item: 'Palak Paneer Combo', original: 155, new: 115, stock: 25, type: 'North Indian', slot: getTimeSlot(19, 21) }
    ],
    'Rasovara': [
      { item: 'Organic Thali', original: 220, new: 160, stock: 18, type: 'Pure Veg', slot: getTimeSlot(18, 20) },
      { item: 'Millet Dosa Set', original: 110, new: 80, stock: 25, type: 'South Indian', slot: getTimeSlot(17, 19) }
    ],
    'The Green Theory': [
      { item: 'Quinoa Buddha Bowl', original: 250, new: 180, stock: 15, type: 'Continental', slot: getTimeSlot(18, 20) },
      { item: 'Vegan Pasta', original: 200, new: 145, stock: 20, type: 'Italian', slot: getTimeSlot(19, 21) }
    ],
    'Green Thaali': [
      { item: 'Unlimited Thali', original: 190, new: 140, stock: 25, type: 'Pure Veg', slot: getTimeSlot(18, 20) },
      { item: 'Mini Meals', original: 120, new: 90, stock: 30, type: 'Pure Veg', slot: getTimeSlot(17, 19) }
    ],
    'Onesta (Veg)': [
      { item: 'Wood Fired Pizza', original: 280, new: 200, stock: 20, type: 'Italian', slot: getTimeSlot(18, 20) },
      { item: 'Pasta Combo', original: 240, new: 175, stock: 22, type: 'Italian', slot: getTimeSlot(19, 21) }
    ],
    'Pure Veg Restaurant': [
      { item: 'South Indian Combo', original: 100, new: 75, stock: 32, type: 'South Indian', slot: getTimeSlot(17, 19) },
      { item: 'North Indian Meal', original: 140, new: 105, stock: 28, type: 'North Indian', slot: getTimeSlot(18, 20) }
    ]
  };

  const templates = dealTemplates[vendor.restaurantName] || [
    { item: 'Special Meal', original: 150, new: 100, stock: 25, type: 'Pure Veg', slot: getTimeSlot(18, 20) }
  ];

  return templates.map(template => ({
    vendorId: vendor._id,
    itemName: template.item,
    description: `Delicious ${template.item} from ${vendor.restaurantName}`,
    originalPrice: template.original,
    newPrice: template.new,
    stockAvailable: template.stock,
    claimed: Math.floor(Math.random() * 5), // 0-4 already claimed
    dealStartTime: template.slot.start,
    dealEndTime: template.slot.end,
    image: vendor.restaurantImage,
    foodType: template.type,
    isActive: true,
    vendor: {
      restaurantName: vendor.restaurantName,
      address: vendor.address,
      location: vendor.location,
      phoneNumber: vendor.phoneNumber,
      googleMapsLocation: vendor.googleMapsLocation,
      rating: 4 + Math.random() // 4.0 to 5.0
    }
  }));
};

// Main seed function
const seedDatabase = async () => {
  try {
    await connectDB();

    // Clear existing data
    console.log('🗑️  Clearing existing data...');
    await User.deleteMany({});
    await Deal.deleteMany({});
    console.log('✅ Existing data cleared');

    // Create vendor accounts
    console.log('👨‍🍳 Creating vendor accounts...');
    const createdVendors = [];
    
    for (const vendorData of vendors) {
      const hashedPassword = await bcrypt.hash(vendorData.password, 10);
      const vendor = await User.create({
        ...vendorData,
        password: hashedPassword
      });
      createdVendors.push(vendor);
      console.log(`   ✓ Created vendor: ${vendor.restaurantName}`);
    }
    console.log(`✅ ${createdVendors.length} vendors created`);

    // Create deals for each vendor
    console.log('🍽️  Creating deals...');
    let totalDeals = 0;
    
    for (const vendor of createdVendors) {
      const deals = createDealsForVendor(vendor);
      await Deal.insertMany(deals);
      totalDeals += deals.length;
      console.log(`   ✓ Created ${deals.length} deals for ${vendor.restaurantName}`);
    }
    console.log(`✅ ${totalDeals} deals created`);

    console.log('\n🎉 Database seeded successfully!');
    console.log('\n📝 Sample Login Credentials:');
    console.log('   Email: mtr@freshbites.com');
    console.log('   Password: vendor123');
    console.log('\n   You can use any vendor email from the list above with password: vendor123\n');

    process.exit(0);
  } catch (error) {
    console.error('❌ Error seeding database:', error);
    process.exit(1);
  }
};

// Run the seed function
seedDatabase();
