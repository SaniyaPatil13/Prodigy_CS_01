def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    text = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: ").strip())
    
    if mode in ['encrypt', 'decrypt']:
        output = caesar_cipher(text, shift, mode)
        print(f"The {mode}ed text is: {output}")
    else:
        print("Invalid mode. Please restart the program.")

if __name__ == "__main__":
    main()
