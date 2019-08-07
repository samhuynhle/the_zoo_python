class Animals:
    def __init__(self,name, health=5, happiness=5):
        self.name = name
        self.health = health
        self.happiness = happiness

    def feed(self):
        self.health += 1
        self.happiness += 1
        
    def display_info(self):
        print(f"Animal Name: {self.name}")

class Lion(Animals):
    def __init__(self, name, health=5, happiness=5):
        super().__init__(name, health, happiness)
        self.diet = "meat"

    def feed(self, diet):
        if diet != self.diet:
            self.health -= 3
            self.happiness -= 3
            print(f"Wrong diet! {self.name} is mad and hungry!")
        else:
            self.health += 1
            self.happiness += 3
            print(f"{self.name} has been fed")
        return self

class Turtle(Animals):
    def __init__(self, name, health=5, happiness=5):
        super().__init__(name, health, happiness)
        self.diet = "greens"

    def feed(self, diet):
        if diet != self.diet:
            self.health -= 1
            self.happiness -= 2
            print(f"Wrong diet! {self.name} is mad and hungry!")
        else:
            self.health += 1
            self.happiness += 3
            print(f"{self.name} has been fed")
        return self

class Tiger(Animals):
    def __init__(self, name, health=5, happiness=5):
        super().__init__(name, health, happiness)
        self.diet = "meat"

    def feed(self, diet):
        if diet != self.diet:
            self.health -= 1
            self.happiness -= 4
            print(f"Wrong diet! {self.name} is mad and hungry!")
        else:
            self.health += 1
            self.happiness += 3
            print(f"{self.name} has been fed")
        return self