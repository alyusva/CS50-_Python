from datetime import date, datetime
import inflect
import sys

def main():
    birthdate = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(1)


    today = date.today()
    minutes = calculate_minutes(birthdate, today)
    print(f"{number_to_words(minutes)} minutes")

def calculate_minutes(birthdate, today):
    delta = today - birthdate
    return round(delta.total_seconds() / 60)

def number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="").replace(" and ", " ")
    return words[0].capitalize() + words[1:]

if __name__ == "__main__":
    main()
