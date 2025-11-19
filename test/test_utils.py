from src.utils import example


def test_example():
    assert example(True)
    assert not example(False)
