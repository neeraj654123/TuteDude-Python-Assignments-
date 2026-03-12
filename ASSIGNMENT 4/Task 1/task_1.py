try:
    # Open the file in read mode
    file = open("sample.txt", "r")
    
    # Read and print each line
    for line in file:
        print(line.strip())
    
    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")