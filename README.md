# SERVANA-Backtend

A backend API server for SERVANA, built with Python (Flask framework), handling routes, models, and database migrations.

---

## Overview

**SERVANA-Backtend** serves as the server-side backbone of the SERVANA application.  
It includes routing logic (`routes/`), data models (`models.py`), extension configurations (`extensions.py`), and application setup (`app.py`).  
It supports database migrations and core services to power the frontend.

---

## Technologies Used

- **Python 3.7+**
- **Flask** – Micro web framework
- **Flask-JWT-Extended** – JWT Authentication
- **SQLAlchemy** – ORM for database models
- **Flask-Migrate** – Database migrations

---

## Getting Started

### Prerequisites

- Python 3.7+ (preferably 3.8+)
- Virtual environment (`venv`)
- A database (SQLite, PostgreSQL, or MySQL)

### Setup Instructions

```bash
git clone https://github.com/Kassim999999/SERVANA-Backtend.git
cd SERVANA-Backtend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the App

Using Flask CLI:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Or run directly:

```bash
python app.py
```

The server should be running at: 👉 `http://127.0.0.1:5000/`

---

## Project Structure

```
SERVANA-Backtend/
├── app.py               # Application entry point
├── extensions.py        # Initialization of Flask extensions
├── models.py            # ORM models
├── routes/              # API endpoint definitions
├── migrations/          # Database migration scripts
├── instance/            # Config files or local settings
├── venv/                # Virtual environment folder
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Authentication

This backend uses **JWT (JSON Web Token)** authentication via `Flask-JWT-Extended`.  
Tokens are issued on login and required for protected routes.

---

## Database & Migrations

- **Flask-Migrate** (with Alembic) handles schema migrations.  
- Run migrations with:  

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---


## License

This project is licensed under the **MIT License**.

---

## Contact

For questions or feedback, feel free to reach out:
email-kassimrooney@gmail.com