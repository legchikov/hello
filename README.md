# Run tests

### Run tests
```
pytest tests/
```

##### [Optional] Run tests with coverage
```
pytest --cov=src tests/
```

##### [Optional] Run tests with coverage (save html report)
```
pytest --cov=src tests/ --cov-report html:reports
```

# Run black (linter)
```
black src
```

# Run isort
```
isort .
```
