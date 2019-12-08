class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
#This next attibute is nested inside the __init__ method (constructor method).
    def eat(self,food):
        if (food == 'apple'):
            self.health -= 100
        else: (food == 'ham')
        self.health += 20

Bob = Hero('Bob')
print (Bob.name)
print (Bob.health)
Bob.eat('apple')
print ("This is Bob's health after eating an apple:", Bob.health)

Bob.eat('ham')
print (Bob.health)
print (Bob.name)

john = Hero('John')
print (john) #This prints the objects ID number.
print (john.name)
print ('\n')

#New __init__ Tutorial
class Tuna:
    def __init__(self): #init functions are looked at first.
        print('Blrbrrbrer') #and this print statement is run first.

    #normal or basic funciton below:
    def swim(self):
        print('I am swimming')

#Object access stuff in a class. The object below is flipper..
#This object is created from the 'Tuna' class
# and then code within the class is run first.
# so 'Blrbrrbrer' is printed first before flipper.swim is run on the next line.
flipper = Tuna()
flipper.swim()
