import pytest
from src.core import run_example


def test_run_example():
    assert run_example(True) == True
    assert run_example(False) == False
