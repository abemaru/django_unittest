import pytest
from sample.helper import small_function

def test_sample_function():
    actual = small_function()
    expected = "this is a sample function!"
    assert actual == expected
