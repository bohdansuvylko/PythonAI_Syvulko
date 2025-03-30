class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("dog", "bark")
        self.name = name
        self.breed = breed

    def fetch(self):
        print(f"{self.name} the {self.breed} fetches the ball.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__("cat", "meow")
        self.name = name
        self.color = color

    def purr(self):
        print(f"{self.name} the {self.color} cat purrs loudly.")

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Orange")

my_dog.make_sound()
my_dog.fetch()

my_cat.make_sound()
my_cat.purr()