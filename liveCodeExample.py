# base class; define without ()
class Animal:
    def __init__(self, species, call, num_of_legs=0, domesticated=False):
        self.species = species
        self.num_of_legs = num_of_legs
        self.domesticated = domesticated
        self.call = call

    def say_something(self):
        return self.call

    def __str__(self):
        return (
            f"This animal is a {self.species} that says {self.say_something()}"
        )



if __name__ == "__main__":
    dog = Animal('dog',"woof", 4, True)
    print(dog)

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__("dog", "Woof", num_of_legs=4, domesticated=True)

    def speak(self):
        return f"Dog goes {self.say_something()}"




if __name__ == "__main__":
    sparky = Dog("Beagle")
    print(sparky)
    print(sparky.speak())


class Pet:
    def __init__(self, name, critter_instance):
        self.name = name
        self.animal_type = critter_instance

    def set_owner(self, name, phone):
        self.owner_name = name
        self.owner_phone = phone

    def __str__(self):
        return f"This pet's name is {self.name}.{self.owner_name} owns this pet. It has {self.animal_type.num_of_legs} legs and it likes to say {self.animal_type.say_something()}!"

standard_poodle = Dog("Standard Poodle")

Choko = Pet("Choko", standard_poodle)
Choko.set_owner("Me", "111-222-3333")

print(Choko)