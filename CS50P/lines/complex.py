def is_even(n):
    """
    Check if a number is even
    """
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(2))  # Should print True
print(is_even(3))  # Should print False
