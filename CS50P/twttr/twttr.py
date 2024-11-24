def main():
    text = input("Input: ")
    result = remove_vowels(text)
    print(f"Output: {result}")

def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return ''.join([char for char in text if char not in vowels])

if __name__ == "__main__":
    main()
