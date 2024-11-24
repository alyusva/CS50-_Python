def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert_to_percentage(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def convert_to_percentage(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

    if x > y or y == 0:
        raise ValueError

    return round((x / y) * 100)

if __name__ == "__main__":
    main()
