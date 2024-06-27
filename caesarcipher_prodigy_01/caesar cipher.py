def caesar_cipher(text, shift, mode):
  result = ""
  for char in text:
    if char.isalpha():
      # Adjust for uppercase/lowercase alphabets
      base = ord('A') if char.isupper() else ord('a')
      # Handle wrapping around the alphabet
      new_ord = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
      new_ord = (new_ord - base) % 26 + base
      result += chr(new_ord)
    else:
      result += char
  return result

def main():
  while True:
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    if mode not in ('encrypt', 'decrypt'):
      print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
      continue
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))
    if shift < 1 or shift > 25:
      print("Invalid shift value. Please enter a number between 1 and 25.")
      continue

    result = caesar_cipher(text, shift, mode)
    print(f"{mode.title()}ed message: {result}")

    # Ask if user wants to continue
    choice = input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
    print("Thank you")
    if choice != 'y':
      break

if __name__ == "__main__":
  main()
