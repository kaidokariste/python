# Actions on the child imply an action on the parent
class Parent(object):

    def implicit(self):
        print("Parent implicit()")

# In child class no new functions are defined but it inherits all
# functions from paren
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()