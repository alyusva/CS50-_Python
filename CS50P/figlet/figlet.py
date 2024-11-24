import sys
import random
import pyfiglet

def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")

    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit("Invalid usage")
        font = sys.argv[2]
        if font not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid usage")
    else:
        font = random.choice(pyfiglet.FigletFont.getFonts())

    text = input("Input: ")
    f = pyfiglet.Figlet(font=font)
    print(f.renderText(text))

if __name__ == "__main__":
    main()
