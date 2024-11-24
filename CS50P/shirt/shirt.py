import sys
import os
from PIL import Image, ImageOps

def main():
    # Verificar el número de argumentos de línea de comandos
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Verificar que los archivos tengan extensiones válidas y coincidentes
    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not (input_path.lower().endswith(valid_extensions) and output_path.lower().endswith(valid_extensions)):
        sys.exit("Invalid input or output format. Must be .jpg, .jpeg, or .png")

    if not input_path.split('.')[-1].lower() == output_path.split('.')[-1].lower():
        sys.exit("Input and output have different extensions")

    # Verificar que el archivo de entrada exista
    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    # Abrir la imagen de entrada y la camiseta
    try:
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")
    except Exception as e:
        sys.exit(f"Error opening image files: {e}")

    # Redimensionar y recortar la imagen de entrada
    try:
        input_image = ImageOps.fit(input_image, shirt_image.size)
    except Exception as e:
        sys.exit(f"Error resizing/cropping input image: {e}")

    # Superponer la camiseta sobre la imagen de entrada
    try:
        input_image.paste(shirt_image, (0, 0), shirt_image)
    except Exception as e:
        sys.exit(f"Error pasting shirt image: {e}")

    # Guardar la imagen resultante
    try:
        input_image.save(output_path)
    except Exception as e:
        sys.exit(f"Error saving output image: {e}")

if __name__ == "__main__":
    main()
