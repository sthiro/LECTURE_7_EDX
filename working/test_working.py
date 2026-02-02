from working import convert
import pytest


def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 AM to 4:30 PM") == "01:00 to 16:30"
    assert convert("12 AM to 12:00 PM") == "00:00 to 12:00"

def test_raise_error():

    with pytest.raises(ValueError):
        convert("1 AM - 4:30 PM")

    with pytest.raises(ValueError):
        convert("1 : 4:30 PM")

    with pytest.raises(ValueError):
        convert("1 AM to 13 PM")

    with pytest.raises(ValueError):
        convert("14 AM to 1 PM")
    
    with pytest.raises(ValueError):
        convert("1 AM to 1:60 PM")

    with pytest.raises(ValueError):
        convert("1:60 AM to 10 PM")

    with pytest.raises(ValueError):
        convert("70:5 AM to 1 PM")

    with pytest.raises(ValueError):
        convert("1 AM : 4:3 PM")

    with pytest.raises(ValueError):
        convert("sample  Text")
    
    