def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid fraction format. X should be less than or equal to Y and both should be integers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero.")

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
