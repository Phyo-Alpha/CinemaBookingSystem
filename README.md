# 🎬 Cinema Booking System

A comprehensive Django-based cinema booking system that allows customers to browse movies, book tickets, select seats, and manage their bookings. The system includes multiple user roles with different levels of access and functionality.

## 🚀 Overview

The Cinema Booking System is a full-featured web application built with Django that simulates a real-world cinema booking experience. It provides a complete solution for movie theater management, including customer bookings, staff operations, and manager administration.

### Key Features

- **Customer Portal**: Browse movies, view details, book tickets, select seats, and manage bookings
- **Staff Interface**: Handle ticket sales, manage food & drinks orders, and assist customers
- **Manager Dashboard**: Complete system administration including movie management, room configuration, and reporting
- **Seat Management**: Dynamic seat selection with real-time availability
- **User Profiles**: Customer profiles with preferences and loyalty points
- **Rating System**: Movie ratings and reviews from customers
- **Responsive Design**: Mobile-friendly interface using Bootstrap

## 🛠️ Technology Stack

- **Backend**: Django 4.2.1 (Python Web Framework)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (default), easily configurable to PostgreSQL/MySQL
- **Forms**: Django Crispy Forms with Bootstrap 5 styling
- **PDF Generation**: xhtml2pdf for ticket generation
- **Image Processing**: Pillow for avatar and movie poster handling
- **Authentication**: Django's built-in authentication system

## 👥 User Roles

### 🎭 Customer
- Browse available movies and showtimes
- View movie details, ratings, and reviews
- Book tickets and select preferred seats
- Manage profile with preferences and loyalty points
- View booking history and purchased tickets

### 🏢 Staff
- Process ticket sales and bookings
- Manage food and drinks orders
- Assist customers with booking issues
- View and manage ticket inventory

### 👨‍💼 Manager
- Complete system administration
- Add/edit/remove movies and showtimes
- Configure cinema rooms and seating
- Manage staff and customer accounts
- Generate reports and analytics
- Set pricing and manage inventory

## 📋 Features

### Core Functionality
- **Movie Management**: Add, edit, and manage movie listings with descriptions, genres, and posters
- **Session Scheduling**: Create and manage movie sessions with different times and rooms
- **Seat Selection**: Interactive seat selection with real-time availability updates
- **Booking System**: Complete booking workflow from movie selection to payment
- **User Authentication**: Secure login/registration with role-based access control
- **Profile Management**: Customer profiles with avatars, preferences, and loyalty points

### Advanced Features
- **Loyalty Points System**: Reward customers with points for bookings
- **Rating & Review System**: Customer feedback and movie ratings
- **Food & Drinks**: Combo meal options for enhanced booking experience
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Admin Dashboard**: Comprehensive management interface for all system operations

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cinema-booking-system.git
   cd cinema-booking-system
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install django==4.2.1
   pip install django-crispy-forms
   pip install django-bootstrap-v5
   pip install crispy-bootstrap5
   pip install xhtml2pdf
   pip install Pillow
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

### Default Login Credentials

After running migrations, you can create user accounts through the registration page or use the Django admin interface at `http://127.0.0.1:8000/admin/` with your superuser credentials.

## 📁 Project Structure

```
CinemaBookingSystem/
├── main/                   # Core application (Customer interface)
├── manager/               # Manager dashboard and administration
├── staff/                 # Staff interface and operations
├── register/             # User authentication and registration
├── media/                # User uploads (avatars, images)
├── static/               # CSS, JS, and static assets
├── templates/            # HTML templates
├── db.sqlite3           # Database file
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 🎯 Usage

### For Customers
1. Register for an account or login
2. Browse available movies
3. Select a movie and choose a showtime
4. Pick your preferred seats
5. Add food & drinks (optional)
6. Complete your booking
7. View your tickets and booking history

### For Staff
1. Login with staff credentials
2. Access the staff dashboard
3. Process customer bookings
4. Manage ticket sales and food orders
5. Assist customers with their bookings

### For Managers
1. Login with manager credentials
2. Access the management dashboard
3. Add/edit movies and showtimes
4. Configure cinema rooms and seating
5. Manage users and generate reports
6. Monitor system performance and bookings

## 🔧 Configuration

### Database Setup
The system uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` configuration in `settings.py`.

### Media Files
User-uploaded files (avatars, movie posters) are stored in the `media/` directory. Configure your web server to serve these files in production.

### Email Configuration
Update the email settings in `settings.py` for password reset and notification features.


