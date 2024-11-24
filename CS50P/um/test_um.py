from um import count
import pytest

def test_single_um():
    assert count("um") == 1

def test_um_with_punctuation():
    assert count("um?") == 1

def test_capital_um():
    assert count("Um, thanks for the album.") == 1

def test_multiple_ums():
    assert count("Um, thanks, um...") == 2

def test_um_as_substring():
    assert count("yummy") == 0

def test_no_um():
    assert count("hello world") == 0

if __name__ == "__main__":
    pytest.main()
