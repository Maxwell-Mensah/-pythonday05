from shark import Shark

class BlueShark(Shark):
    def eat(self, animal):
        if animal.species_type=="fish":
            print(f"{self.name} ate a {animal.species_type} named {animal.name}")
            if frenzy:
                frenzy=False
        else:
            print(f"{animal.name}: It's not worth my time")