import sys
import os
import csv
from tabulate import tabulate

def main():
    # Verificar el número de argumentos de línea de comandos
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <filename>")
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    # Verificar que el archivo tiene extensión .csv
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Verificar que el archivo existe
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    # Leer el archivo CSV y formatearlo como tabla ASCII
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
    except Exception as e:
        sys.exit(f"Could not read file: {e}")

if __name__ == "__main__":
    main()
