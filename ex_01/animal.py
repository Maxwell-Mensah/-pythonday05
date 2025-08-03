class Animal:
    MAMMAL=0
    FISH=1
    BIRD=2
    __TYPES = {
        MAMMAL: "mammal",
        FISH: "fish",
        BIRD: "bird"
    } #dictionnaire privé qui fait la correspondance int → str
    def __init__(self, name, legs, type):
        self.name=name
        self.legs=legs
        self.species_type = Animal.__TYPES.get(type, "unknown") #permet de renvoyer "unknown" si on passe une valeur non reconnue
        print(f"My name is {self.name} and I am a {self.species_type}")
    
    def getName(self):
        return self.name

    def getLegs(self):
        return self.legs

    def getType(self):
        return self.species_type

