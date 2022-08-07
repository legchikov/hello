from cProfile import run
from src.hello.services.index import run_index


def test_run_index():
    assert run_index() == [1, 2, 3]
