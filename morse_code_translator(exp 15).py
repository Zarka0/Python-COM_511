# Create a python program to implement morse code translator

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}
def text_to_morse(text):
    morse_code = ' '.join(morse_code_dict[char.upper()] for char in text)
    return morse_code

def morse_to_text(morse_code):
    reverse_dict = {value: key for key, value in morse_code_dict.items()}
    morse_code_split = morse_code.split(' ')
    text = ''.join(reverse_dict[code] for code in morse_code_split)
    return text

while True:
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        text_input = input("Enter the text to convert to Morse code: ")
        morse_result = text_to_morse(text_input)
        print(f"Morse Code: {morse_result}")

    elif choice == '2':
        morse_input = input("Enter the Morse code to convert to text: ")
        text_result = morse_to_text(morse_input)
        print(f"Text: {text_result}")

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")