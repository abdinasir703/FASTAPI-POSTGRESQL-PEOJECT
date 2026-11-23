# FastAPI PostgreSQL Backend

An **intermediate-level backend project** built with Python, FastAPI, and PostgreSQL. This project demonstrates how to build a REST API, connect it to a relational database, and implement CRUD operations.

## Features

- FastAPI REST API
- PostgreSQL database integration
- Database connection testing
- Table creation
- Create, read, update, and delete users
- Interactive API documentation with Swagger UI
- Git and GitHub version control

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Git & GitHub

##  Project Structure

```text
FASTAPI-POSTGRESQL-PEOJECT/
│
├── main.py
├── .gitignore
└── README.md
```

##  Setup

### 1. Clone the Repository

```bash
git clone https://github.com/abdinasir703/FASTAPI-POSTGRESQL-PEOJECT.git
cd FASTAPI-POSTGRESQL-PEOJECT
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn psycopg2-binary
```

### 3. Configure PostgreSQL

Create a PostgreSQL database named:

```text
Backend_database
```

Configure the application with your PostgreSQL credentials.

> **Security:** Never upload your PostgreSQL password or other secrets to GitHub.

## Run the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

##  API Documentation

FastAPI provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the documentation to test the API endpoints directly from your browser.

##  API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check that the API is running |
| GET | `/db-test` | Test the PostgreSQL connection |
| GET | `/create-table` | Create the users table |
| GET | `/add-user` | Add a user |
| GET | `/users` | Retrieve users |
| PUT | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |

##  Database

This project uses **PostgreSQL** as its relational database.

### Database

```text
Backend_database
```

### Users Table

| Column | Type | Description |
|---|---|---|
| `id` | SERIAL | Primary key |
| `name` | VARCHAR(100) | User name |
| `age` | INTEGER | User age |

##  CRUD Operations

The project demonstrates the four fundamental database operations:

- **Create** — Add new users
- **Read** — Retrieve users
- **Update** — Modify existing users
- **Delete** — Remove users

##  Learning Objectives

This project demonstrates practical experience with:

- Python backend development
- FastAPI
- REST API development
- PostgreSQL database integration
- CRUD operations
- API testing with Swagger UI
- Git and GitHub

##  Project Level

**Intermediate Backend Project**

## Author

**Abdinasir Adan**

Aspiring Backend Software Engineer


## FINALLY
-" Every project teaches me something new . Im not just building projects-am becoming a strong software eng

## if you find this project helpful, fell free to star the repo



**Focus:** Python • FastAPI • PostgreSQL • Backend Development
