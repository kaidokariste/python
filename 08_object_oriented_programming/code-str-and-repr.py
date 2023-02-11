class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is how to make string representation of object, otherwise you print and get <__main__.Person object at 0x0000025CC3F4CA60>
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    # By default always str is shown first. repr is used on debugging and when __str__ does not exist
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)
print(bob.__repr__())
