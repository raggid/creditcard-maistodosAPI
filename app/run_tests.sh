export TEST=True
pipenv run alembic upgrade head
pipenv run python test_database.py
pipenv run pytest tests
unset TEST
rm ./tests/test.db