from sys import argv

# argument values definitions to pass
script, input_file = argv

# function to print all the file
def print_all(f):
    print(f.read())

# rewinf back the file pointer
def rewind(f):
    # This moves pointer back to start of a file
    f.seek(0)

# print every line one by one
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1 <- this was original
# same thing can be done using +=
current_line += 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)