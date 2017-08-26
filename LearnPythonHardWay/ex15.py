#  imports module argv
from sys import argv

# defines argument variables that the script waits before execution
script, filename = argv

# try to open file, that is defined in filename
txt = open(filename)

# Prints out the name of file and also prints the content
# that read function reads from file
print("Here's your file: {}".format(filename))
print(txt.read())

#  Type inside the script tha filename
print("Type the filename again:")
file_again = input("> ")

# Try to open just printed file
txt_again = open(file_again)

# Print out the content of new file
print(txt_again.read())
