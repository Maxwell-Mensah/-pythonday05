from animal import Animal

class Cat(Animal):
    def __init__(self, name, color="grey", legs=4, type=Animal.MAMMAL):
        super().__init__(name, legs, type)
        self.color=color
        print(f"{self.name}: MEEEOOWWWW")

    def get_color(self):
        return self.color
        
    def set_color(self, new_color):
        self.color=new_color

    def meow(self):
        print(f"{self.name} the color {self.color} kitty is meowing")


isidore = Cat("Isidore", "orange")
print(f"{isidore.getName()} has {isidore.getLegs()} legs and is a {isidore.getType()}.")
isidore.meow()
