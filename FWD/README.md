# 🍽️ FreshBites - Reduce Food Waste, Grow Your Business# 🍽️ FreshBites - Food Waste Reduction Platform# 🍽️ FreshBites - Food Waste Reduction Platform



## Overview

FreshBites is a platform connecting Pure Veg food vendors with customers in Bangalore to reduce food waste by offering surplus food at discounted prices. Vendors can turn their surplus inventory into profit while contributing to sustainability.

> **A modern, minimal MERN stack application connecting local food businesses with consumers to reduce food waste while providing affordable meal options in Bangalore, India.**[![MERN Stack](https://img.shields.io/badge/Stack-MERN-green.svg)](https://github.com/facebook/create-react-app)

## ✨ Key Features

[![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen.svg)](https://www.mongodb.com/)

### For Vendors

- 🏪 Easy vendor registration and profile management## ✨ Features[![Node.js](https://img.shields.io/badge/Runtime-Node.js-green.svg)](https://nodejs.org/)

- 📝 Create and manage daily deals

- 💰 Set discounted prices for surplus food[![React](https://img.shields.io/badge/Frontend-React-blue.svg)](https://reactjs.org/)

- 📊 Real-time stock management

- 📞 Direct customer communication- 🌈 **Modern UI** with glassmorphism design and smooth animations[![Express.js](https://img.shields.io/badge/Backend-Express.js-lightgrey.svg)](https://expressjs.com/)

- 🗺️ Google Maps integration for location

- 🎯 **Browse Deals** from 15+ Bangalore restaurants [![Docker](https://img.shields.io/badge/Deployment-Docker-blue.svg)](https://www.docker.com/)

### For Customers

- 🔍 Browse active deals from Pure Veg restaurants- 💰 **INR Pricing** with ₹ symbol throughout

- 💚 Get discounts on quality surplus food

- ⏰ View pickup times and availability- 🥗 **Jain Food Options** clearly marked> **A production-ready MERN stack application connecting local food businesses with consumers to reduce food waste while providing affordable meal options in Bangalore, India.**

- 📍 Easy restaurant location access

- 🌱 Contribute to reducing food waste- 📍 **Location-based** deals across Bangalore



## 🛠️ Tech Stack- 👤 **User Authentication** with JWT## 🌟 Features



**Frontend:**- 🏪 **Vendor Dashboard** for deal management

- React 18.2.0

- React Router 6.8.0### 🎨 **Production Optimizations**

- Axios for API calls

- Modern CSS with responsive design## 🛠️ Tech Stack- ⚡ **Performance**: Gzip compression, caching, code splitting



**Backend:**- 🔒 **Security**: Helmet.js headers, rate limiting, CORS protection

- Node.js with Express

- MongoDB with Mongoose- **Frontend**: React.js with modern CSS- 🐳 **Docker Ready**: Complete containerization with nginx load balancer

- JWT Authentication

- bcryptjs for password encryption- **Backend**: Node.js + Express.js- 📊 **Monitoring**: Health checks, error boundaries, comprehensive logging



## 📋 Prerequisites- **Database**: MongoDB + Mongoose- 🚀 **Deployment**: One-command production deployment with Docker Compose



Before you begin, ensure you have the following installed:- **Authentication**: JWT

- **Node.js** (v14 or higher) - [Download](https://nodejs.org/)

- **MongoDB** (running locally or MongoDB Atlas account) - [Download](https://www.mongodb.com/try/download/community)### For Consumers

- **npm** (comes with Node.js)

## 🚀 Quick Start- 🌈 **Beautiful Homepage** with hero section and smooth animations

## 🚀 Installation & Setup

- 🎯 **Browse Deals** from 15+ famous Bangalore restaurants 

### Step 1: Clone the Repository

```bash### Prerequisites- 💰 **Proper INR Pricing** with ₹ symbol throughout

git clone <repository-url>

cd FreshBites-main- Node.js (v18+)- 🥗 **Jain Food Options** clearly marked with green indicators

```

- MongoDB- 📍 **Location-based** deals across Bangalore localities

### Step 2: Install Dependencies

```bash- npm- ⏰ **Real-time** pickup time slots and availability

# Install all dependencies (root, frontend, and backend)

npm run install-all- 👤 **User Authentication** with secure JWT-based sessions

```

### Installation- 🛡️ **Error Handling** with graceful error boundaries and loading states

### Step 3: Configure MongoDB Connection



**Option A: Local MongoDB**

- Ensure MongoDB is running on `mongodb://localhost:27017/freshbites`1. **Clone and install**### For Vendors  

- Default configuration is already set in `backend/server.js`

   ```bash- 🏪 **Vendor Dashboard** for complete deal management

**Option B: MongoDB Atlas (Cloud)**

1. Create a `.env` file in the `backend` directory:   git clone <your-repo>- ➕ **Create Deals** with images, pricing, and details

```

MONGODB_URI=your_mongodb_atlas_connection_string   cd FreshBites-main- 📊 **Track Performance** with real-time analytics

JWT_SECRET=your_secure_jwt_secret_here

PORT=5000   npm run install-all- 🍽️ **Food Categories** across 5 cuisine types

```

   ```- 🟢 **Jain Options** specification for inclusive dining

### Step 4: Seed the Database with Sample Data

- ⏰ **Flexible Timing** for pickup windows

**On Windows (PowerShell):**

```powershell2. **Environment Setup**

.\seed.bat

```   ```bash## 🛠️ Tech Stack



**On Linux/Mac (Bash):**   # Backend environment

```bash

chmod +x seed.sh   cd backend| Component | Technology | Purpose |

./seed.sh

```   cp .env.example .env|-----------|------------|---------|



**Alternative (from backend directory):**   # Edit .env with your MongoDB URI| **Frontend** | React.js | User interface with error boundaries |

```bash

cd backend   ```| **Backend** | Node.js + Express.js | RESTful API with security middleware |

npm run seed

```| **Database** | MongoDB + Mongoose | Data storage with connection pooling |



This will populate your database with:3. **Start Development**| **Authentication** | JWT | Secure user sessions |

- **18 Pure Veg restaurants** in Bangalore

- **36 sample deals** with various food items   ```bash| **Security** | Helmet.js + Rate Limiting | Production-grade security |

- All vendors with password: `vendor123`

   npm run dev| **Deployment** | Docker + Docker Compose | Containerized deployment |

### Step 5: Start the Application

   ```| **Load Balancer** | Nginx | Reverse proxy with SSL termination |

**From the root directory:**

```bash| **Styling** | Pure CSS | Responsive design with animations |

npm run dev

```   - Backend: http://localhost:5000| **Currency** | INR (₹) | Indian Rupee formatting |



This command will concurrently start:   - Frontend: http://localhost:3000

- ✅ Backend server on `http://localhost:5000`

- ✅ Frontend development server on `http://localhost:3000`## 🚀 Quick Start



Your browser should automatically open to `http://localhost:3000`## 📁 Project Structure



## 🔑 Sample Login Credentials### Prerequisites



After seeding the database, you can login with any of these vendor accounts:```- **Node.js** (v18.0.0 or higher)



**Email Format:** `[restaurant-name]@freshbites.com`FreshBites/- **MongoDB** (v7.0 or higher) or MongoDB Atlas

**Password:** `vendor123` (for all accounts)

├── backend/                    # Node.js API- **Docker & Docker Compose** (for production deployment)

**Example Logins:**

- Email: `mtr@freshbites.com` | Password: `vendor123`│   ├── models/                # MongoDB schemas- **npm** package manager

- Email: `sagar@freshbites.com` | Password: `vendor123`

- Email: `mavalli-tiffin@freshbites.com` | Password: `vendor123`│   ├── routes/                # API endpoints



**Complete Vendor List (18 Restaurants):**│   ├── server.js              # Main server### Development Setup

1. mtr@freshbites.com

2. sagar@freshbites.com│   └── package.json           # Backend deps

3. vasudev@freshbites.com

4. mavalli-tiffin@freshbites.com├── frontend/                   # React app1. **Clone the repository**

5. vidyarthi@freshbites.com

6. brahmins@freshbites.com│   ├── src/                   # React source   ```bash

7. shanthi@freshbites.com

8. taaza-thindi@freshbites.com│   │   ├── components/        # UI components   git clone https://github.com/your-username/freshbites.git

9. veena@freshbites.com

10. annapoorna@freshbites.com│   │   ├── pages/            # Route pages   cd freshbites

11. anand@freshbites.com

12. udupi@freshbites.com│   │   └── index.css         # Modern CSS   ```

13. karavalli@freshbites.com

14. shivaji@freshbites.com│   └── package.json          # Frontend deps

15. dasaprakash@freshbites.com

16. koshy@freshbites.com└── package.json               # Root scripts2. **Install all dependencies**

17. vidyarthi-bhavan@freshbites.com

18. central@freshbites.com```   ```bash



## 📁 Project Structure   npm run install-all



```## 🎨 Design Features   ```

FreshBites-main/

├── frontend/                 # React frontend application

│   ├── public/

│   │   └── index.html- **Glassmorphism UI** with backdrop filters3. **Set up environment variables**

│   ├── src/

│   │   ├── components/      # Reusable components- **Gradient animations** and smooth transitions   

│   │   │   ├── DealCard.js  # Deal display card

│   │   │   ├── DealModal.js # Deal details modal- **Modern cards** with hover effects   Create `.env` file in `backend/` directory:

│   │   │   ├── Header.js

│   │   │   ├── ErrorBoundary.js- **Responsive design** for all devices   ```env

│   │   │   ├── LoadingSpinner.js

│   │   │   └── ProtectedRoute.js- **Contemporary color scheme** with vibrant gradients   MONGODB_URI=mongodb://localhost:27017/freshbites

│   │   ├── contexts/        # React contexts

│   │   │   └── AuthContext.js   JWT_SECRET=your_super_secret_jwt_key_here_min_32_chars

│   │   ├── pages/          # Page components

│   │   │   ├── HomePage.js## 📊 API Endpoints   NODE_ENV=development

│   │   │   ├── DealsPage.js

│   │   │   ├── DealDetailsPage.js   PORT=5000

│   │   │   ├── LoginPage.js

│   │   │   ├── RegisterPage.js| Method | Endpoint | Description |   ```

│   │   │   ├── VendorDashboard.js

│   │   │   ├── VendorProfile.js|--------|----------|-------------|

│   │   │   ├── AddDeal.js

│   │   │   └── ManageDeals.js| POST | `/api/auth/register` | User registration |4. **Start MongoDB service**

│   │   ├── styles/         # CSS files

│   │   ├── App.js| POST | `/api/auth/login` | User login |   ```bash

│   │   └── index.js

│   └── package.json| GET | `/api/deals` | Get all deals |   # On Windows

├── backend/                 # Express backend application

│   ├── models/| POST | `/api/deals` | Create deal (vendor) |   net start MongoDB

│   │   ├── User.js         # Vendor user model

│   │   └── Deal.js         # Deal model| GET | `/api/vendors/:id` | Get vendor profile |   

│   ├── routes/

│   │   ├── auth.js         # Authentication routes   # On macOS (with Homebrew)

│   │   ├── deals.js        # Deal CRUD routes

│   │   └── vendors.js      # Vendor profile routes## 🚀 Deployment   brew services start mongodb-community

│   ├── seedData.js         # Database seeding script

│   ├── server.js           # Express server setup   

│   └── package.json

├── seed.sh                 # Linux/Mac seeding scriptSimple deployment options:   # On Linux

├── seed.bat                # Windows seeding script

├── package.json            # Root package.json- **Backend**: Heroku, Railway, Render   sudo systemctl start mongod

└── README.md

```- **Frontend**: Netlify, Vercel   ```



## 🔄 Available Scripts- **Database**: MongoDB Atlas



**Root Directory:**5. **Seed the database with sample data**

- `npm run install-all` - Install all dependencies

- `npm run dev` - Start both frontend and backend servers## 📄 License   ```bash

- `npm run server` - Start only backend server

- `npm run client` - Start only frontend client   npm run seed

- `npm run seed` - Seed database with sample data

MIT License   ```

**Frontend Directory:**

- `npm start` - Start React development server

- `npm run build` - Create production build

- `npm test` - Run tests---6. **Start the development servers**



**Backend Directory:**   ```bash

- `npm run dev` - Start server with nodemon (auto-reload)

- `npm start` - Start server normally**Built with ❤️ for reducing food waste in Bangalore**   npm run dev

- `npm run seed` - Seed database   ```



## 🌐 API Endpoints   This starts:

   - **Backend**: http://localhost:5000

### Authentication   - **Frontend**: http://localhost:3000

- `POST /api/auth/register` - Register new vendor

- `POST /api/auth/login` - Vendor login## 📁 Project Structure



### Vendors```

- `GET /api/vendors/profile` - Get vendor profile (protected)FreshBites/

- `PUT /api/vendors/profile` - Update vendor profile (protected)├── 📁 backend/                 # Node.js/Express API server

│   ├── 📁 models/             # MongoDB schemas (User, Deal)

### Deals│   │   ├── User.js            # User model with vendor profiles

- `GET /api/deals` - Get all active deals│   │   └── Deal.js            # Deal model with INR currency

- `GET /api/deals/:id` - Get single deal│   ├── 📁 routes/             # API endpoints

- `POST /api/deals` - Create new deal (vendor only)│   │   ├── auth.js            # Authentication routes

- `PUT /api/deals/:id` - Update deal (vendor only)│   │   ├── deals.js           # Deal CRUD operations

- `DELETE /api/deals/:id` - Delete deal (vendor only)│   │   └── vendors.js         # Vendor management

- `GET /api/deals/vendor/mydeals` - Get vendor's deals (vendor only)│   ├── server.js              # Main server configuration

│   ├── seedData.js           # Database seeding script

## 🎨 Color Scheme│   ├── .env                  # Environment variables

│   └── package.json          # Backend dependencies

- **Primary Green:** `#10b981` - Main brand color├── 📁 frontend/               # React.js client application

- **Dark Green:** `#059669` - Hover states│   ├── 📁 public/            # Static assets

- **Dark Text:** `#064e3b` - Headings│   ├── 📁 src/               # React source code

- **Light Text:** `#6b7280` - Body text│   │   ├── 📁 components/    # Reusable UI components

- **Background:** White and light green gradients│   │   │   ├── Header.js     # Navigation header

- **Accent:** `#dc2626` - Discount badges│   │   │   └── DealCard.js   # Deal display component

│   │   ├── 📁 pages/         # Page components

## 🔒 Security Features│   │   │   ├── HomePage.js       # Landing page with hero

│   │   │   ├── DealsPage.js      # Deal browsing page

- JWT-based authentication│   │   │   ├── DealDetailsPage.js # Individual deal view

- Password hashing with bcryptjs│   │   │   ├── LoginPage.js      # User authentication

- Protected routes for vendors│   │   │   ├── RegisterPage.js   # User registration

- HTTP-only token storage│   │   │   └── VendorDashboard.js # Vendor management

- Profile completion validation│   │   ├── App.js            # Main app with routing

│   │   ├── index.js          # React entry point

## 🚢 Deployment│   │   └── index.css         # Global styles with animations

│   └── package.json          # Frontend dependencies

### Frontend Deployment (Vercel/Netlify)├── .github/                  # GitHub configuration

1. Build the frontend:│   └── copilot-instructions.md # AI development guidelines

```bash├── .gitignore               # Git ignore rules

cd frontend├── package.json             # Root package.json with scripts

npm run build├── PROJECT_OVERVIEW.html    # Demo showcase page

```└── README.md               # This file

```

2. Deploy the `build` folder to your hosting service

## 🎯 Available Scripts

3. Set environment variable for API URL:

```| Command | Description |

REACT_APP_API_URL=your_backend_url|---------|-------------|

```| `npm run dev` | Start both frontend and backend concurrently |

| `npm run server` | Start only the backend server (port 5000) |

### Backend Deployment (Render/Heroku)| `npm run client` | Start only the frontend server (port 3000) |

1. Ensure MongoDB Atlas is configured| `npm run install-all` | Install dependencies for both frontend and backend |

| `npm run seed` | Populate database with sample deals and restaurants |

2. Set environment variables:| `npm run build` | Build frontend for production |

```

MONGODB_URI=your_mongodb_atlas_uri## 🍴 Food Categories & Restaurants

JWT_SECRET=your_production_jwt_secret

PORT=5000### Cuisine Types

NODE_ENV=production- 🥘 **South Indian**: Dosa, Idli, Vada, Uttapam, Filter Coffee

```- 🍛 **North Indian**: Roti, Sabzi, Biryani, Thali, Chole Bhature  

- 🍕 **Italian**: Pizza, Pasta, Lasagna

3. Deploy with the start script from `backend/package.json`- 🥢 **Chinese**: Manchurian, Chilli Paneer, Hakka Noodles

- 🥗 **Continental**: Sandwiches, Salads, Mediterranean Bowls

## 🐛 Troubleshooting

### Featured Restaurants (15+)

**Issue: MongoDB connection error**- **Vidyarthi Bhavan** (Basavanagudi) - Famous for Benne Masala Dosa

- Ensure MongoDB is running: `mongod` command- **MTR** (Lalbagh) - Legendary South Indian breakfast

- Check connection string in `.env` or `server.js`- **Brahmins Coffee Bar** (Basavanagudi) - Traditional filter coffee

- **Taaza Thindi** (Jayanagar) - Fresh South Indian snacks

**Issue: Port already in use**- **Shanti Sagar** (Malleshwaram) - North Indian specialties

- Change PORT in backend `.env` file- **Udupi Palace** (Rajajinagar) - Authentic Udupi cuisine

- Kill existing process using the port- And 10+ more authentic Bangalore establishments



**Issue: Deals not showing**### Locations Covered

- Ensure database is seeded: `npm run seed`📍 **Jayanagar** • **Basavanagudi** • **Malleshwaram** • **Rajajinagar** • **Hanumanthanagar** • **Lalbagh**

- Check backend console for errors

## 🔧 API Endpoints

**Issue: Login not working**

- Clear browser cache/cookies### Authentication

- Ensure backend server is running- `POST /api/auth/register` - User registration

- Check MongoDB connection- `POST /api/auth/login` - User login



## 📝 License### Deals

- `GET /api/deals` - Get all deals with INR formatting

This project is for educational purposes.- `GET /api/deals/:id` - Get specific deal details  

- `POST /api/deals` - Create new deal (vendors only)

## 👥 Support- `PUT /api/deals/:id` - Update existing deal

- `DELETE /api/deals/:id` - Delete deal

For issues or questions, please create an issue in the repository.- `POST /api/deals/:id/claim` - Claim a deal



---### Vendors

- `GET /api/vendors` - Get all vendor profiles

**Made with ❤️ for reducing food waste in Bangalore**- `GET /api/vendors/:id` - Get specific vendor

- `PUT /api/vendors/:id` - Update vendor profile

## 💰 Currency Implementation

FreshBites uses **Indian Rupee (₹)** throughout the application:

- **Backend**: Stores numerical values with `currency: 'INR'` field
- **API Responses**: Include `formattedPrice: ₹${amount}` for display
- **Frontend**: Consistent ₹ symbol rendering with `.currency-inr` CSS class
- **Database**: All monetary fields stored as numbers for calculations

## 🟢 Jain Food Support

Special accommodation for Jain dietary requirements:
- **Clear Marking**: Green 🟢 indicators on Jain-friendly items
- **Database Field**: `isJain: Boolean` field in deal schema
- **Filtering**: Easy identification during browsing
- **Vendor Options**: Ability to specify Jain compliance during deal creation

## 🎨 UI/UX Features

### Animations & Interactions
- **Smooth Transitions**: 0.3s ease animations on hover states
- **Loading States**: Spinner animations for data fetching
- **Card Hover Effects**: Elevation changes with shadow enhancement
- **Responsive Design**: Mobile-first approach with grid layouts

### Design System
- **Color Palette**: Green primary (#4CAF50) representing freshness
- **Typography**: System fonts with proper hierarchy
- **Spacing**: Consistent 8px grid system
- **Components**: Reusable cards, buttons, and form elements

## 🔒 Security Features

- **JWT Authentication**: Secure token-based sessions
- **Password Hashing**: bcryptjs for secure password storage
- **Input Validation**: Server-side validation with express-validator
- **CORS Configuration**: Proper cross-origin resource sharing
- **Environment Variables**: Sensitive data protection

## 🚀 Deployment

### 🐳 Production Deployment with Docker (Recommended)

**Quick Production Deployment:**

```bash
# 1. Setup production environment
npm run production:setup

# 2. Deploy with Docker
npm run production:deploy

# 3. Check deployment status
npm run docker:logs
```

**Manual Docker Deployment:**

```bash
# 1. Clone and configure
git clone <your-repo-url>
cd FreshBites-main

# 2. Setup environment files
cp backend/.env.production backend/.env
cp frontend/.env.production frontend/.env

# 3. Update environment variables with your values
# Edit backend/.env and frontend/.env

# 4. Deploy all services
docker-compose up -d

# 5. Check service status
docker-compose ps
```

**Available Docker Services:**
- **Frontend**: React app with nginx (Port 3000)
- **Backend**: Node.js API server (Port 5000) 
- **Database**: MongoDB with authentication (Port 27017)
- **Load Balancer**: Nginx reverse proxy (Port 80/443)

**Production URLs:**
- **Frontend**: http://localhost or your domain
- **API**: http://localhost/api or your-domain.com/api
- **Health Check**: http://localhost/api/health

### 🔧 Manual Deployment

1. **Database Setup**
   ```bash
   # MongoDB Atlas (Recommended)
   # Create cluster at https://cloud.mongodb.com
   # Update MONGODB_URI in .env
   ```

2. **Environment Variables**
   ```env
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/freshbites
   JWT_SECRET=your_super_secure_jwt_secret_key_minimum_32_characters
   NODE_ENV=production
   PORT=5000
   ```

3. **Build Frontend**
   ```bash
   npm run build
   ```

4. **Deployment Platforms**
   - **Backend**: Heroku, Railway, DigitalOcean, AWS EC2
   - **Frontend**: Netlify, Vercel, AWS S3 + CloudFront
   - **Database**: MongoDB Atlas (recommended)

## 📊 Production Monitoring

### Health Checks
```bash
# Check application health
npm run health:check

# View service logs
npm run docker:logs

# Monitor resource usage
docker stats
```

### Available Endpoints
- **Health Check**: `/api/health` - Application and database status
- **API Status**: `/` - API information and endpoints
- **Frontend**: `/` - React application with error boundaries

### Backup and Maintenance
```bash
# Database backup
npm run backup:db

# Restart services
npm run docker:restart

# Clean up resources
npm run clean
```

## 🔒 Security Features

**Production Security Hardening:**
- 🛡️ **Helmet.js**: Security headers and CSP
- ⚡ **Rate Limiting**: API endpoint protection
- 🔐 **JWT Authentication**: Secure token-based sessions
- 🔒 **Password Hashing**: bcryptjs with salt rounds
- 🌐 **CORS Protection**: Configurable origin whitelist
- 📝 **Input Validation**: Express-validator middleware
- 🐳 **Docker Security**: Non-root user containers
- 🔄 **Error Handling**: Graceful error boundaries

**Security Checklist:**
```bash
# Run security audit
./security-check.sh

# Check for vulnerabilities
npm audit

# Update dependencies
npm update
```

## 🧪 Testing

### Manual Testing Checklist
- ✅ User registration and login
- ✅ Deal browsing with proper INR display
- ✅ Deal claiming functionality  
- ✅ Vendor dashboard access
- ✅ Deal creation and management
- ✅ Error handling and loading states
- ✅ Responsive design across devices
- ✅ Security headers and rate limiting

### Production Readiness
- ✅ Docker containerization with multi-stage builds
- ✅ nginx load balancer with SSL/TLS support
- ✅ Database connection pooling and authentication
- ✅ Environment-based configuration
- ✅ Health checks and monitoring endpoints
- ✅ Security hardening and vulnerability scanning

## 📚 Documentation

- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Comprehensive production deployment guide
- **[.github/copilot-instructions.md](./.github/copilot-instructions.md)** - Development guidelines
- **[security-check.sh](./security-check.sh)** - Security audit script

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Local Bangalore Restaurants** for inspiration on real venues
- **MERN Stack Community** for excellent documentation
- **Open Source Contributors** for making this possible

---

**Built with ❤️ for reducing food waste in Bangalore**

🌱 *Together, let's make every meal count and build a sustainable future!*
- ✅ Image loading with fallbacks
- ✅ Responsive design on mobile
- ✅ Jain food filtering
- ✅ Currency formatting consistency

### Performance Optimization
- **Image Optimization**: WebP format with fallbacks
- **Code Splitting**: React lazy loading for routes
- **Database Indexing**: Optimized queries for deals
- **Caching**: Static asset caching strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow the existing code style and structure
- Add proper error handling and validation
- Update documentation for new features
- Test thoroughly before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bangalore Restaurant Community** for inspiration
- **MongoDB** for flexible data storage
- **React Team** for the amazing frontend framework
- **Express.js** for the robust backend framework
- **Unsplash** for high-quality food photography

## 📞 Support

For support, email support@freshbites.in or create an issue in this repository.

---

**Made with ❤️ for reducing food waste in Bangalore**

*FreshBites - Connecting communities, reducing waste, one meal at a time.*
