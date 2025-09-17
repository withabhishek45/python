# Open the source file in read mode
with open("sorce.txt", "r") as source:
    content = source.read()  

# Open the destination file in write mode and write the content
with open("dest.txt", "w") as destination:
    destination.write(content)  

print("Content copied successfully!")
print("File content: ",content) 