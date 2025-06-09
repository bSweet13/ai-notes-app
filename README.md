# Flask API Project

A Flask-based REST API project with a clean architecture and testing setup.

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
python run.py
```

The server will start on http://localhost:5001

## Available Endpoints

- `GET /health` - Health check endpoint that returns `{"status": "ok"}`

## Running Tests

To run tests:
```bash
python -m pytest
```
