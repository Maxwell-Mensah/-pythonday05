from shark import Shark

class Greatwhite(Shark):
    def eat(self, animal):
        if type(animal).__module__=="canary":
            print(f"{self.name}: Next time you try to give me that to eat, I'll eat you instead")
        elif type(animal).__module__=="shark":
            print(f"{self.name}: The best meal one could wish for")
        else:
            super().eat(animal) #utiliser la version parente de eat
            