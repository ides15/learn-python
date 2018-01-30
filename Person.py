class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        return "Name: %s, age: %i" % self.name, self.age