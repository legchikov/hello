from src.hello.services.index import run_index, run_super_index


def test_run_index():
    assert run_index() == [1, 2, 3]

def test_run_super_index():
    assert run_super_index() == [1, 2, 3, 4, 5]

