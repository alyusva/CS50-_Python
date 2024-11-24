import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Expresión regular para encontrar el valor del atributo src en un iframe
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"', s)
    if match:
        # Extraer la URL del match
        url = match.group(1)
        # Transformar la URL a su versión corta
        video_id = url.split('/')[-1]
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
