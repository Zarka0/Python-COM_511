# Create a text file "MyFile.txt" in python and ask the user to write seprate three lines with three input statement from the user

with open("MyFile.txt", "w") as file:
    for i in range(3):
        line = input(f"Enter line {i + 1}: ")
        file.write(line + "\n")
        
with open("MyFile.txt", "r") as file:
    file_content = file.read()
    print("\nContent of MyFile.txt:")
    print(file_content)