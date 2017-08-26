name = 'Kaido Kariste'
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
