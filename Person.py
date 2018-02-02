class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return "Name: %s, age: %i" % (self.name, self.age)