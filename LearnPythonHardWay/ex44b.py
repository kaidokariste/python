# Actions on the child override the action on the parent.

class Parent(object):

    def override(self):
        print("PARENT override()")

# using in child class the same function name as in parent
# overrides the parent function
class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()