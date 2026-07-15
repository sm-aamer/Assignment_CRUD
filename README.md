# Patients Management System

A simple FastAPI-based Patients Management System with CRUD endpoints for patients.

## Project Structure

Patients_Management_System/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   │   ├── patient.py
│   ├── schemas/
│   │   ├── patient.py
│   ├── crud/
│   │   ├── patient.py
│   ├── routes/
│   │   ├── patient.py
│   └── utils/
├── alembic/
├── requirements.txt
└── README.md

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   pip install -r requirements.txt
3. Create a MYSQL database named assignment_curd_db.
4. Set the database URL if needed:
5. Start the app:
   uvicorn app.main:app --reload

## Database Notes

- The app is configured to use MySQL by default.
- Set the DATABASE_URL environment variable before starting the app if you want to use a different MySQL server.
- Example:
  $env:DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>"
- If MySQL is not reachable, the app will still start, but database initialization will fail until the server is available.
- Alembic is included for later migrations.

## API Endpoints

- GET /docs for Swagger UI
- GET /patients/
- POST /patients/
