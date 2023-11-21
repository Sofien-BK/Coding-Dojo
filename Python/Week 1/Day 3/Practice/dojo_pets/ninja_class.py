#CLASS Ninja 
class Ninja:
    def __init__(self, first_name,last_name,treats,pet_food,pet) :
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    def walk(self):
        self.pet.play()   # walk() - walks the ninja's pet invoking the pet play() method
    def feed(self):
        self.pet.eat()   # feed() - feeds the ninja's pet invoking the pet eat() method
    def bath(self):
        self.pet.noise() # bathe() - cleans the ninja's pet invoking the pet noise() method
