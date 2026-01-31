from numb3rs import validate


def test_single_digit():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

    assert validate("-1.1.1.1") == False
    assert validate("50.2") == False

    