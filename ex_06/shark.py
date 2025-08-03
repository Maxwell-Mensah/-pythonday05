from animal import Animal

class Shark(Animal):
    def __init__(self,name, legs=0, type=Animal.FISH, _frenzy=False):
        super().__init__(name, legs, type)
        self.frenzy=_frenzy
        print("A KILLER IS BORN")

    def smellBlood(self, value:bool):
        self.frenzy=value

    def status(self):
        if self.frenzy:
            print(f"{self.name} is smelling blood and wants to kill")
        else:
            print(f"{self.name} is swimming peacefully")

    def eat(self, animal):
        if type(animal).__module__=="animal":
            print(f"{self.name} ate a {animal.species_type} named {animal.name}")
            if frenzy:
                frenzy=False
        else:
            print(f"{animal.name}: It's not worth my time")