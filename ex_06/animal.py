class Animal:
    MAMMAL=0
    FISH=1
    BIRD=2
    count=0
    nb_mammals=0
    nb_fish=0
    nb_bird=0
    __TYPES = {
        MAMMAL: "mammal",
        FISH: "fish",
        BIRD: "bird"
    } #dictionnaire privé qui fait la correspondance int → str
    def __init__(self, name, legs, type):
        Animal.count+=1
        self.name=name
        self.legs=legs
        self.species_type = Animal.__TYPES.get(type, "unknown") #permet de renvoyer "unknown" si on passe une valeur non reconnue
        print(f"My name is {self.name} and I am a {self.species_type}")
        match self.species_type:
            case "mammal":
                Animal.nb_mammals+=1
            case "fish":
                Animal.nb_fish+=1
            case "bird":
                Animal.nb_bird+=1
    
    def getName(self):
        return self.name

    def getLegs(self):
        return self.legs

    def getType(self):
        return self.species_type

    @classmethod
    def getNumberOfAnimalsAlive(cls):
        print(f"There {"is" if cls.count<2 else 'are'} currently {cls.count} animal{'s' if cls.count<2 else ''} alive in our world")
    
    @classmethod
    def getNumberOfMammals(cls):
        print(f"There {"is" if cls.nb_mammals<2 else 'are'} currently {cls.nb_mammals} mammal{'' if cls.nb_mammals<2 else 's'} alive in our world") 

    @classmethod
    def getNumberOfFishes(cls):
        print(f"There {"is" if cls.nb_fish<2 else 'are'} currently {cls.nb_fish} fish{'' if cls.nb_fish<2 else 'es'} alive in our world") 

    @classmethod
    def getNumberOfBirds(cls):
        print(f"There {"is" if cls.nb_bird<2 else 'are'} currently {cls.nb_bird} bird{'' if cls.nb_bird<2 else 's'} alive in our world") 