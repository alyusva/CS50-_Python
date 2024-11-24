import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)

def convert(s):
    # Definir el patrón de expresión regular para coincidir con los formatos de tiempo
    pattern = r"^(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError

    start_time, start_period, end_time, end_period = match.group(1), match.group(3), match.group(4), match.group(6)

    # Convertir los tiempos a formato de 24 horas
    start_24 = to_24_hour_format(start_time, start_period)
    end_24 = to_24_hour_format(end_time, end_period)

    return f"{start_24} to {end_24}"

def to_24_hour_format(time, period):
    # Separar horas y minutos
    parts = time.split(':')
    hours = int(parts[0])
    minutes = int(parts[1]) if len(parts) > 1 else 0

    # Validar horas y minutos
    if hours < 1 or hours > 12 or minutes < 0 or minutes >= 60:
        raise ValueError

    if period == "AM" and hours == 12:
        hours = 0
    elif period == "PM" and hours != 12:
        hours += 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
