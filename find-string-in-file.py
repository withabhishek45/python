# Program to find a string in a given file

#   search word by user
search_word = input("Enter the word to search: ")

# Open the file in read mode
with open("example.txt", "r") as file:
    lines = file.readlines()

found = False

# Check each line for the search word
for line_no, line in enumerate(lines, start=1):
    if search_word in line:
        print(f"Found '{search_word}' in line {line_no}: {line.strip()}")
        found = True

if not found:
    print(f"'{search_word}' not found in the file.")
