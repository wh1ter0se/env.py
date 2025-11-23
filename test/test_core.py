from envpy import run_example


def test_run_example():
    assert run_example(True)
    assert not run_example(False)
