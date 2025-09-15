🎬 Online Movie Booking System

This project is a Django-based Movie Ticket Booking System where users can browse movies, view details, select seats, and confirm their bookings.

🚀 Features

📍 Browse Movies by Location

🎥 View Movie Details (poster, rating, show timings, theatre info)

🪑 Interactive Seat Selection (unavailable seats are blocked)

✅ Booking Confirmation with seat details and total price calculation

🏠 Back to Home Navigation


🏠 Home Page

Users can select a location from the dropdown. Available movies are displayed with their posters, names, and ratings.

<img width="1920" height="697" alt="Home" src="https://github.com/user-attachments/assets/d3e16a11-0444-4afa-ae38-b31b8776b869" />
🎬 Movie Details Page

When a movie is selected, users can view details such as poster, description, and available theatres.

<img width="1919" height="793" alt="Movie details" src="https://github.com/user-attachments/assets/a52531bf-7277-429c-95c3-4759599daa01" />
🪑 Seat Selection Page

Users can choose seats from the theatre’s seat layout. Already booked seats are disabled/unavailable.

<img width="1919" height="762" alt="Seat Selection" src="https://github.com/user-attachments/assets/23a3b86a-a18c-4cf1-8c1b-54bcbb46fccc" />
✅ Booking Confirmation Page

After selecting seats, users are shown a confirmation page with:

🎥 Movie Poster & Name

🎭 Theatre Name & Show Time

🪑 Selected Seats

💰 Price Calculation (with tax)

🔙 Option to go back to Home

<img width="680" height="909" alt="Booking Confirmation" src="https://github.com/user-attachments/assets/bb8ee671-e040-4aff-8a09-e523ea695f60" />
🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS (Django Templates)

Database: SQLite (default, can be swapped with PostgreSQL/MySQL)

📖 How to Run

Clone the repository

git clone <your-repo-url>
cd OnlineMovieBooking


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Start the development server

python manage.py runserver


Open in browser

http://127.0.0.1:8000/

🎯 Future Enhancements

Online payment gateway integration 💳

User booking history 📜

Admin panel for managing shows 🎭
