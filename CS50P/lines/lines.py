import sys
import os

def main():
    # Verificar el número de argumentos de línea de comandos
    if len(sys.argv) != 2:
        print("Usage: python lines.py <filename>")
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    # Verificar que el archivo tiene extensión .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Verificar que el archivo existe
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    # Contar las líneas de código
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        sys.exit(f"Could not read file: {e}")

    loc = count_lines_of_code(lines)
    print(loc)

def count_lines_of_code(lines):
    loc = 0
    for line in lines:
        stripped_line = line.strip()
        # Ignorar líneas en blanco y comentarios
        if stripped_line and not stripped_line.startswith("#"):
            loc += 1
    return loc

if __name__ == "__main__":
    main()
