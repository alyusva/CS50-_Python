from seasons import calculate_minutes, number_to_words
from datetime import date

def test_calculate_minutes():
    assert calculate_minutes(date(2023, 7, 23), date(2024, 7, 23)) == 527040
    assert calculate_minutes(date(2022, 7, 23), date(2024, 7, 23)) == 1052640

def test_number_to_words():
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert number_to_words(1051200) == "One million, fifty-one thousand, two hundred"

if __name__ == "__main__":
    import pytest
    pytest.main()
