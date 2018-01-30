from Person import Person

class Employee(Person):
    numEmployee = 0

    def __init__(self, name, age, rate):
        Person.__init__(self, name, age)
        self.owed = 0
        self.rate = rate
        Employee.numEmployee += 1

    def __repr__(self):
        return "A custom Employee object for %s" % self.name

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return "%.2f hours worked" % numHours

    def pay(self):
        self.owed = 0
        return "payed %s" % self.name