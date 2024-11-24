def main():
    names = []

    print("Enter names, one per line (press Ctrl-D to end input):")
    while True:
        try:
            name = input().strip()
            if name:
                names.append(name)
        except EOFError:
            break

    print(generate_farewell(names))

def generate_farewell(names):
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

if __name__ == "__main__":
    main()
