from numb3rs import validate


def test_single_digit():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

    assert validate("-1.1.1.1") == False
    assert validate("5.2") == False
    assert validate("1") == False

def test_double_digit():
    assert validate("17.10.90.64") == True
    assert validate("10.0.0.40") == True
    assert validate("15.2.3.4") == True

    assert validate("10.10") == False
    assert validate("-41.1.1.1") == False
    assert validate("00.0.0.0") == False
    assert validate("*10.0.0.25") == False

def test_triple_digit():
    assert validate("192.168.1.6") == True
    assert validate("127.0.0.1") == True
    assert validate("100.1.90.255") == True

    assert validate("-41.1.1.1") == False
    assert validate("0.0.0.256") == False
    assert validate("127.500.2.12") == False

def test_input_type():
    assert validate("cat") == False
    assert validate("") == False