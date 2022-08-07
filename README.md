# Run tests
pytest tests/

### Run tests with coverage
pytest --cov=src tests/

### Run tests with coverage (save html report)
pytest --cov=src tests/ --cov-report html:reports

# Run black (linter)
black src

# Run isort
isort .