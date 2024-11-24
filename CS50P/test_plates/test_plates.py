from plates import is_valid

def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("CS50") == True
    assert is_valid("ABCDE") == True
    assert is_valid("XY1234") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_starts_with_letters():
    assert is_valid("123ABC") == False
    assert is_valid("1A2B3C") == False

def test_valid_characters():
    assert is_valid("AB@123") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False

def test_ends_with_numbers_if_any():
    assert is_valid("AB012") == False  # No debe empezar con '0' en la parte numérica
    assert is_valid("ABC12A") == False  # No debe tener letras después de la primera parte numérica
    assert is_valid("ABC123") == True  # Correcto

def test_no_leading_zero():
    assert is_valid("AB0123") == False  # Número no debe comenzar con 0
    assert is_valid("ABC001") == False  # Número no debe comenzar con 0

def test_only_letters():
    assert is_valid("ABCDEF") == True  # Correcto
    assert is_valid("ABCDE1") == True  # Correcto
    assert is_valid("ABC123") == True  # Correcto

def test_edge_cases():
    assert is_valid("AB") == True  # Longitud mínima válida
    assert is_valid("A2") == False  # No debe tener un solo caracter antes del número
    assert is_valid("AB12") == True  # Correcto
    assert is_valid("A1234") == False  # No debe comenzar con un solo carácter

def test_numbers_in_middle():
    assert is_valid("AB12CD") == False  # Números en medio no son válidos
    assert is_valid("ABCD12") == True  # Correcto
    assert is_valid("ABC12D") == False  # Letras después de números no son válidos

