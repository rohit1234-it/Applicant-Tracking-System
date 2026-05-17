# 🧑‍💼 Applicant Tracking System (ATS) – Django REST API

A full-stack Applicant Tracking System built using Django and Django REST Framework.  
The system supports secure authentication (JWT), job posting, candidate applications, skill-based scoring, and notification management.

This project simulates a real-world recruitment platform similar to Naukri/LinkedIn hiring modules.

---

# 🚀 Live Demo
👉 https://your-live-link.pythonanywhere.com/

---

# 🔐 Authentication

This project uses **JWT (JSON Web Token)** authentication for secure API access.

## Features:
- User Login / Token generation
- Protected API endpoints
- Role-based access (Admin / Candidate - if implemented)
- Secure request handling using Bearer Token

---

# 📁 Project Structure


ATS_SYSTEM/
│
├── ATS_SYSTEM/ # Project settings (Django config)
├── jobs/ # Job management app (API + views)
├── candidates/ # Candidate application system
├── notifications/ # Notification system
├── templates/ # Frontend HTML pages
├── static/ # CSS & JavaScript files
├── db.sqlite3 # Database
├── manage.py
├── requirements.txt


---

# ⚙️ Features

## 💼 Job Module
- Create jobs with title and required skills
- View all available jobs
- REST API for job management

## 👨‍💻 Candidate Module
- Apply for jobs with name, email, and skills
- Store applications in database
- Skill-based matching system

## 📊 Skill Matching System
- Compares candidate skills with job requirements
- Generates match percentage score
- Returns sorted candidate list based on score

## 🔔 Notification System
- Notification generated on job application
- View all notifications via API/UI
- Timestamp tracking for each event

## 🌐 Frontend UI
- Job listing page
- Candidate list page with scores
- Notification display page

---

# 🛠️ Tech Stack

- Python 3
- Django 5.x
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite Database
- HTML, CSS, JavaScript

---

# 📦 Installation & Setup

## 1. Clone Repository
```bash
git clone https://github.com/yourusername/ATS_SYSTEM.git
cd ATS_SYSTEM
2. Create Virtual Environment
python -m venv env
env\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run Migrations
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
python manage.py createsuperuser
6. Run Server
python manage.py runserver
🔗 API Endpoints
🔹 Authentication
POST /api/token/ → Get JWT token
POST /api/token/refresh/ → Refresh token
🔹 Jobs API
GET /api/jobs/ → List all jobs
POST /api/jobs/ → Create job (protected)
🔹 Candidates API
GET /api/candidates/ → List candidates
POST /api/candidates/ → Apply for job
🔹 Notifications API
GET /api/notifications/ → View notifications
📊 Project Highlights

✔ Full-stack ATS system using Django REST Framework
✔ JWT-based authentication system
✔ Skill-based candidate scoring algorithm
✔ Notification system for job applications
✔ Modular architecture (jobs, candidates, notifications apps)
✔ Live deployment on PythonAnywhere

🎯 Future Improvements
Resume upload & parsing (PDF support)
Advanced AI-based candidate ranking
Role-based dashboards (HR / Candidate UI)
Pagination & search filters
Email notifications system
👨‍💻 Author

Rohit Kasar
Python Developer | Django & REST API Enthusiast


---

# 🚀 Use this like this:

1. Save file as:
```text
README.md
Push to GitHub:
git add README.md
git commit -m "Add professional README with JWT support"
git push
