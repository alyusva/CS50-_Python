import emoji

def main():
    text = input("Input: ")
    emojized_text = emoji.emojize(text, language='alias')
    print(f"Output: {emojized_text}")

if __name__ == "__main__":
    main()
