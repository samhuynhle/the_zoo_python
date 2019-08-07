import animals

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,species,name):
        self.animals.append(species(name))
        return self
    def print_all_animals(self):
        print("-"*20, self.zoo_name, "-"*20)
        for animal in self.animals:
            animal.display_info()
        return self
    def feed_animal(self,animal_name, diet):
        for x in self.animals:
            if x.name == animal_name:
                x.feed(diet)
                return self
            else:
                print(f"No animal named {animal_name}")
                return self