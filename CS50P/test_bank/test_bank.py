from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello there") == 0
    assert value("Hello, Newman") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How you doing?") == 20

def test_other():
    assert value("what's happening?") == 100
    assert value("good morning") == 100
    assert value("Greetings") == 100

def test_case_insensitivity():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hi") == 20
    assert value("HEY") == 20
    assert value("What's happening?") == 100
    assert value("GOOD MORNING") == 100

def test_leading_spaces():
    assert value(" hello") == 0
    assert value(" Hello, Newman") == 0
    assert value(" hi") == 20
    assert value(" hey") == 20
    assert value(" what's happening?") == 100
    assert value(" good morning") == 100

