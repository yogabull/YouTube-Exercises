#Python Object-Oriented Programming - Corey Shafer Tutorial

#NOTE: methods are functions associated with a class.

# I think it's convention to capitalize class names.
# classes pass variables and attibutes together..
# init method used to initialize the class.
# init is known as a constructor in other languages..
# Constructor is a function RUN when class instance is created..
class Employee:

        def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Yoga', 'Bull', '50')
emp_2 = Employee('Slime', 'Woof', '70')

print (emp_1)
print (emp_2)

print(emp_2.fullname)
print(Employee.fullname(emp_1))

print('{} {}'.format(emp_1.first, emp_1.last))


'''
NOTE about classes:
A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts.
'''
