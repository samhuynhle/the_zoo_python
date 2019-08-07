class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_lion(self,name):
        self.animals.append(Lion(name))
        return self
    def add_turtule(self,name):
        self.animals.append(Turtle(name))
        return self
    def add_tiger(self,name):
        self.animals.append(Tiger(name))
        return self
    def print_all_animals(self):
        print("-"*20, self.zoo_name, "-"*20)
        for animal in self.animals:
            animal.display_info()
        return self

class Animals:
    def __init__(self,name, health=5, happiness=5):
        self.name = name
        self.health = health
        self.happiness = happiness

    def feed(self):
        self.health += 1
        self.happiness += 1
    def display_info(self):
        print(f"Animal Name: {self.name}, Animal Health: {self.health}, Animal Happiness: {self.happiness}.")

class Lion(Animals):
    def __init__(self, name, health=5, happiness=5):
        super().__init__(name, health, happiness)
        self.diet = "meat"

    def feed(self, diet):
        if diet != self.diet:
            self.health -= 1
            self.happiness -= 5
        else:
            self.health += 1
            self.happiness += 3

class Turtle(Animals):
    def __init__(self, name, health=5, happiness=5):
        super().__init__(name, health, happiness)
        self.diet = "greens"

    def feed(self, diet):
        if diet != self.diet:
            self.health -= 1
            self.happiness -= 5
        else:
            self.health += 1
            self.happiness += 3

class Tiger(Animals):
    def __init__(self, name, health=5, happiness=5):
        super().__init__(name, health, happiness)
        self.diet = "meat"

    def feed(self, diet):
        if diet != self.diet:
            self.health -= 1
            self.happiness -= 5
        else:
            self.health += 1
            self.happiness += 3

seattle = Zoo('Seattle Zoo')
print(seattle.zoo_name)
seattle.add_lion('Big Lion').add_tiger('Fat Tiger').add_turtle('Armored Reptile')

