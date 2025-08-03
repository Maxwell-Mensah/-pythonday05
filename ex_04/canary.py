from animal import Animal

class Canary(Animal):
    def __init__(self,name, legs=2, type=Animal.BIRD, _eggs=0):
        super().__init__(name, legs, type) #héritage des attributs de la class mère qu'est Animal
        self.egg=_eggs
        print("Yellow and smart? Here I am !")

    #définiton des méthodes propres a la class Canary
    def getEggsCount(self):
        return self.egg

    def layEgg(self):
        self.egg+=1

