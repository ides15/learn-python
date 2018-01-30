from Employee import Employee

john = Employee("John", 33.25)

print(john.owed)
print(john.hours(40))
print(john.owed)
print(john.pay())
print(john.owed)

print(Employee.numEmployee)

print(john)