def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted) if mode == "encode" else chr(start +
                                                                        (shifted - shift) % 26)
        else:
            result += char
    return result


def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encode or decode? ").lower()

    if choice == "encode" or choice == "decode":
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        encoded_text = caesar_cipher(text, shift, choice)
        print("Encoded/Decoded Text:", encoded_text)
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")


if __name__ == "__main__":
    main()
