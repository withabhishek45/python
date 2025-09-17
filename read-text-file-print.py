with open("text.txt", "r") as file:
    # Read all lines from the file
    content = file.read()
print(content)  

no_of_lines=content.splitlines()
print("The number of lines in the file is:",len(no_of_lines))

no_of_words=content.split()
print("The number of words in the file is:",len(no_of_words))

no_ofchar=len(content)
print("The number of characters in the file is:",no_ofchar)


