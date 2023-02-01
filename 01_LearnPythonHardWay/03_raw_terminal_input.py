print("How old are you"),
age = input()  # raw_input from python2 was renamed input in python3
print("How tall are you"),
height = input()
print("How much do you weight"),
weight = input()

print("So you're {} old, {} tall and {} heavy.".format(age,height,weight))

# you can define input text also as variable
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weight? ")

print("So, you're {} old, {} tall and {} heavy. ".format(age,height,weight))