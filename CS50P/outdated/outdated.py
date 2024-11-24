def main():
    while True:
        date_input = input("Date: ").strip()  # Strip leading and trailing spaces
        try:
            iso_date = convert_to_iso(date_input)
            if iso_date:
                print(iso_date)
                break
        except ValueError:
            continue

def convert_to_iso(date_str):
    import re

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Check for MM/DD/YYYY format
    if re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', date_str):
        month, day, year = map(int, date_str.split('/'))
    else:
        # Check for Month DD, YYYY format
        match = re.match(r'^(\w+) (\d{1,2}), (\d{4})$', date_str)
        if match:
            month_str, day, year = match.groups()
            if month_str in months:
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)
            else:
                raise ValueError
        else:
            raise ValueError

    # Validate the month and day
    if 1 <= month <= 12 and 1 <= day <= 31:
        return f"{year:04}-{month:02}-{day:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
