# 1. Take user input and write it to a file
data = input("Enter some text to write in the file: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

# 2. Append additional data to the same file
extra = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(extra + "\n")
file.close()

# 3. Read and display the final content of the file
file = open("output.txt", "r")
print("\nFinal content of the file:")
print(file.read())
file.close()