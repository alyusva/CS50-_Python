import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Usar una expresión regular para encontrar "um" como palabra completa, case-insensitive
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
