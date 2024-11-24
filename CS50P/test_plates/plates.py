def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
        has_valid_length(s) and
        starts_with_letters(s) and
        has_valid_characters(s) and
        ends_with_numbers_if_any(s)
    )

def has_valid_length(s):
    return 2 <= len(s) <= 6

def starts_with_letters(s):
    return s[:2].isalpha()

def has_valid_characters(s):
    return s.isalnum()

def ends_with_numbers_if_any(s):
    if not any(char.isdigit() for char in s):
        return True

    number_part_started = False
    for char in s:
        if char.isdigit():
            number_part_started = True
            if char == '0' and s[s.index(char) - 1].isdigit() is False:
                return False
        elif number_part_started:
            return False
    return True

if __name__ == "__main__":
    main()
