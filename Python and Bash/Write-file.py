# Open a file in write mode
file = open("sample.txt", "w")

# Write content to the file
file.write("Hello, this is my first file.\n")
file.write("This file is created using Python.\n")

# Close the file
file.close()

print("Content written to file successfully.")