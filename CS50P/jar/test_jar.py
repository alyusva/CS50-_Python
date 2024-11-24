import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(15)
    assert jar.capacity == 15
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("ten")

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪"

    jar.withdraw(2)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)

if __name__ == "__main__":
    pytest.main()
