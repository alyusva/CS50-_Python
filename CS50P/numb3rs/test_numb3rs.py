from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True

def test_invalid_addresses():
    assert validate("275.3.6.28") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("123.456.78.90") == False
    assert validate("1.2.3.-1") == False
    assert validate("1.2.3.256") == False
    assert validate("cat") == False
    assert validate("123.123.123") == False
    assert validate("123.123.123.123.123") == False
    assert validate("...") == False
    assert validate("256.256.256.256") == False
    assert validate("a.b.c.d") == False

if __name__ == "__main__":
    import pytest
    pytest.main()
