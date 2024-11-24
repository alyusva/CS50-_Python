import pytest
from fuel import convert, gauge

def test_convert():
    # Pruebas exitosas
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

    # Pruebas que deberían lanzar ValueError
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")

    # Pruebas que deberían lanzar ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    # Pruebas exitosas
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

    # Pruebas límite
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"

if __name__ == "__main__":
    pytest.main()
