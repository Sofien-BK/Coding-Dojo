from ninja_class import Ninja
#class pet
class Pet:
    def __init__(self,name,type,tricks,health,energy):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    def sleep (self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health+=10
    def play(self):
        self.health += 5
    def noise(self):
        print(f'the sound of {self.name}')
cat=Pet('teber','cat','talk',100,10)
sofien=Ninja('sofien','ben khedher','kroket','salami',cat)

sofien.walk()
sofien.feed()
sofien.bath()
#Sub classes by Inheritance 
class Tiger(Pet):
    def __init__(self, name, type, tricks, health, energy , damage):
        super().__init__(name, type, tricks, health, energy)
        self.damage=damage


tiger=Tiger('chiko', 'tiger','killing',1000,200,50)


