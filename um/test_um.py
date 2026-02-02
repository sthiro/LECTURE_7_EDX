from um import count
import pytest

def test_normal():
    assert count("um") == 1
    assert count("um.") == 1
    assert count("um?") == 1
    assert count(" um ") == 1

def test_sentence():
    assert count("hi um my name is thiroshan um...") == 2
    assert count("this is my umbrella ") == 0

def test_case():

    assert count("UM") == 1
    assert count("Um thanks") == 1
    assert count("Um thanks for the food um....") == 2

def test_rother():

    with pytest.raises(TypeError):
        count(56)
    with pytest.raises(TypeError):
        count()

