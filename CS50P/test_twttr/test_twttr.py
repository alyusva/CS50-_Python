from twttr import shorten

def test_shorten():
    # Test cases for removing vowels
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hello") == "Hll"
    assert shorten("hElLo") == "hlL"

    # Test cases for strings without vowels
    assert shorten("bcdfgh") == "bcdfgh"
    assert shorten("BCDFGH") == "BCDFGH"

    # Test cases for empty string
    assert shorten("") == ""

    # Test cases for strings with only vowels
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

    # Test cases for mixed characters
    assert shorten("12345") == "12345"
    assert shorten("!@#$%") == "!@#$%"
    assert shorten("hello123") == "hll123"
    assert shorten("HELLO123") == "HLL123"
    assert shorten("hello!") == "hll!"
    assert shorten("HELLO!") == "HLL!"

def test_shorten_special_cases():
    # Test cases with special characters and spaces
    assert shorten("Hello") == "Hll"
    assert shorten("H_e_l_l_o") == "H__l_l_"
    assert shorten("A quick brown fox.") == " qck brwn fx."
    assert shorten("THE QUICK BROWN FOX.") == "TH QCK BRWN FX."
    assert shorten("This is a test.") == "Ths s  tst."
    assert shorten("TESTING, 1, 2, 3!") == "TSTNG, 1, 2, 3!"
