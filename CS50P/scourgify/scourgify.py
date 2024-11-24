import sys
import csv

def main():
    # Verificar el número de argumentos de línea de comandos
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input.csv output.csv")
        sys.exit("Too few or too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Verificar que el archivo de entrada puede ser leído
    try:
        with open(input_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            students = list(reader)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # Procesar y escribir el archivo de salida
    try:
        with open(output_file, mode='w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                last, first = student["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": student["house"]})
    except Exception as e:
        sys.exit(f"Could not write to {output_file}: {e}")

if __name__ == "__main__":
    main()
