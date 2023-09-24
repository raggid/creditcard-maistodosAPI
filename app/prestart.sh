#! /usr/bin/env bash

# Let the DB start
python await_database.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python initial_data.py

# Start the Application
 uvicorn main:app --host 0.0.0.0 --port 8000