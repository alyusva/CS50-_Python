import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Patrón regex para una dirección IPv4 válida
    pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
    # Verificar si la dirección coincide con el patrón
    if not pattern.match(ip):
        return False

    # Verificar que cada octeto esté en el rango de 0 a 255
    octets = ip.split(".")
    for octet in octets:
        if not (0 <= int(octet) <= 255):
            return False

    return True

if __name__ == "__main__":
    main()
