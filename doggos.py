'''
Animals have a name, energy level, hunger level, and mood
    eat
    sleep

Dogs have breeds
    play

Cats have coat color
    hunt
'''


class Dog:
    # Documentation
    name: str
    energy: int
    hungry: bool
    mood: str

    # Method because it is a function in a class
    # __init__ is a constructor (kind of)
    # Constructor constructs instances
    # Attributes are like name, energy, hungry, mood
    # Self is not passed in
    # The type of self is the same as the type of the class ex. self is type Dog here
    # class is making a type!
    def __init__(self, the_name: str):
        self.name = the_name
        self.energy = 0
        self.hungry = False
        self.mood = "happy"

    def feed(self):
        self.hungry = True

    def play_with_my_dog(self):
        self.mood = "happy"
        self.hungry = True
        self.energy -= 1

    def rest(self, length_of_time: int):
        self.energy += length_of_time
# Creates an instance of Dog
ada = Dog("Ada")
babbage = Dog("Babbage")

ada.rest(8)
ada.play_with_my_dog()
ada.feed()
ada.rest(5)
babbage.mood = ada.mood
