import zoo
import animals

seattle = zoo.Zoo('Old Seattle Zoo')
seattle.add_animal(animals.Turtle,'Green Back').add_animal(animals.Turtle,'Big Shell').print_all_animals()
seattle.feed_animal('Green Back','greens')
print(seattle.animals[0].happiness)
print(seattle.animals[1].happiness)
