from animal import Animal

class Shark(Animal):
    def __init__(self,name, legs=0, type=Animal.FISH, _frenzy=False):
        super().__init__(name, legs, type) #héritage des attributs de la classe mère qu'est Animal
        self.frenzy=_frenzy
        print("A KILLER IS BORN")

    #définition des méthodes propres à la class Shark
    def smellBlood(self, value:bool): 
        self.frenzy=value

    def status(self):
        if self.frenzy:
            print(f"{self.name} is smelling blood and wants to kill")
        else:
            print(f"{self.name} is swimming peacefully")