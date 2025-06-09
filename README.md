# Flask API Project

A Flask-based REST API project with a clean architecture, PostgreSQL database integration, and testing setup.

## Prerequisites

- Python 3.9+
- PostgreSQL 14+
- pip

## Database Setup

1. Install PostgreSQL (on macOS using Homebrew):
```bash
brew install postgresql@14
brew services start postgresql@14
createuser -s postgres
```

2. Create development and test databases:
```bash
python create_dbs.py
```

## Project Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python init_db.py
```

## Environment Variables

Create a `.env` file in the project root with the following variables:
```
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_notes_dev
TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_notes_test
```

## Running the Application

Start the development server:
```bash
python run.py
```

The server will start on http://localhost:5001

## Available Endpoints

- `GET /health` - Health check endpoint that returns `{"status": "ok"}`

## Database Models

### User
- `id` (Integer, Primary Key)
- `email` (String, Unique)
- `cognito_sub` (String, Unique)
- `created_at` (DateTime)

## Running Tests

To run all tests:
```bash
python -m pytest
```

To run specific tests:
```bash
python -m pytest tests/test_models.py -v  # Run model tests
python -m pytest tests/test_health.py -v  # Run health endpoint tests
```

## Project Structure

```
ai-notes-app/
├── app/
│   ├── __init__.py      # Application factory and extensions
│   ├── models.py        # Database models
│   └── routes.py        # API endpoints
├── tests/
│   ├── __init__.py
│   ├── test_health.py   # Health endpoint tests
│   └── test_models.py   # Database model tests
├── config.py            # Configuration settings
├── create_dbs.py        # Database creation script
├── init_db.py          # Database initialization script
├── requirements.txt     # Project dependencies
└── run.py              # Application entry point
```
