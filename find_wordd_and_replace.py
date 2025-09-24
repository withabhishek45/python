word=input("Enter the word to be found: ")
replaced_word=input("Enter the word to replace: ")

with open("sample.txt","r") as file:
    content=file.read()
    new_content=content.replace(word,replaced_word)

with open("sample.txt","w") as file:
    file.write(new_content)

print("All occurrences of the word have been replaced.")

