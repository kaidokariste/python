# Create variable x with one formatting of value '10'
x = "There are {} types of people".format(10)  # maybe 4th SIS
# Two other string variables
binary = "binary"
do_not = "don't"
# Same as x but it uses previous variables as formatting strings
y = "Those who know {} and those who {}.".format(binary, do_not) # 1. String inside string (SIS)

# Print them out
print(x)
print(y)

# Seems to be like nested formatting is also possible
print("I said: {}".format(x))  # 2. SIS
# Nested formatting inside quote marks
print("I also said: '{}'.".format(y))  # 3. SIS

# One Boolean value and one string variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Combining boolean value and string variable as formatting string
print(joke_evaluation.format(hilarious))

# Just put together two strings as one
w = "This is the left side of ..."
e = "a string with a right side"

print(w + e)
