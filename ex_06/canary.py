from animal import Animal

class Canary(Animal):
    def __init__(self,name, legs=2, type=Animal.BIRD, _eggs=0):
        super().__init__(name, legs, type)
        self.egg=_eggs
        print("Yellow and smart? Here I am !")

    def getEggsCount(self):
        return self.egg

    def layEgg(self):
        self.egg+=1

