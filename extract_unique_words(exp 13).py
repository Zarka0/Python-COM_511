# Write a program that input a text file. The program should print all of the unique word in the file in alphabetical order

def extract_unique_words(file_path):
    unique_words = set()

    # Open the file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into words and add them to the set
            words = line.split()
            unique_words.update(words)

    return sorted(unique_words)

def main():
    # Input the path of the text file
    file_path = input("Enter the path of the text file: ")

    try:
        # Extract unique words and print them in alphabetical order
        unique_words = extract_unique_words(file_path)
        print("\nUnique words in alphabetical order:")
        for word in unique_words:
            print(word)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()