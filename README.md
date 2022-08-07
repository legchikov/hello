# Run tests
pytest tests/

# Run tests with coverage
pytest --cov=src tests/

# Run black (linter)
black src

# Run isort
isort .