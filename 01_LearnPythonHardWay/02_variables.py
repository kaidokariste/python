# Variables and names
# Defining variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Concating variables into string
print(f"There are {cars} cars available.")
print("There are only",drivers, "drivers available")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")

name = 'Kaido'
age = 31  # not a lie
height = 181  # cm
weight = 89  # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Formattimise muster python3 puhul on '{} {}'.format('üks','kaks')
# python 2 kasutab %s nagu õpikus näidatud
print("Let's talk about {}.".format(name))
print("He's {} cm tall.".format(height))
print("He's {} kg heavy".format(weight))
print("Actually it's not too heavy")
print("He's got {} eyes and {} hair.".format(eyes,hair))
print("His teeth are usually {} depending on the coffee.".format(teeth))

# This is tricky try to get it right
print("If I add {}, {}, and {} I get {}.".format(age,height,weight,(age+height+weight)))

# Creating some headers
print('*'*10 + 'Escape characters' + '*'*10)

tabby_cat = "\tI'm tabbed in."  # \t on tab ehk tabulaator
height = "I am 6'2\" tall."  # escape double-quote inside string
persian_cat = "I'm split \non a line"  # Line break caracter
backslash_cat = "I'm \\ a \\ cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(height)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Defining formatter separately
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter, formatter, formatter, formatter)
print(formatter.format(
                        "I had this thing.",
                        "That you could type up right.",
                        "But it didn't sing.",
                        "So I said goodnight."
                       )
      )
