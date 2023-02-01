# Run it in terminal using arguments
# $ python ex13.py til tol tal

from sys import argv  # this what we import is called a "module"

script, first, second, third = argv  # argument variable

print("The script is called", script)
print("Your first variable is: ", first)
print("Your second variable is", second)
print("Your third variable is", third)

# Additional user inbut besides script variables
name = input("what is your name?")

print("So, good job {} !".format(name))


