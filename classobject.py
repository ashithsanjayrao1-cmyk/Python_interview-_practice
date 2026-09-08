# class Dog:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} says Woof!")       


# dog1 = Dog("Dicchi Guru","German Shephard") 

# dog2 = Dog("Luna", "Siberian Husky")

# dog1.bark()
# dog2.bark()

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)

#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} is barking")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} says meow!")


# my_dog = Dog("Dicchi Gutu","Rottwiller")
# my_cat = Cat("Luna")

# my_dog.bark()

# my_dog.eat()
# my_dog.sleep()

# my_cat.eat()
# my_cat.sleep()

# my_cat.meow()

class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow!")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says moo!")


my_dog = Dog("Dicchi Guru")
my_cat = Cat("Luna")
my_cow = Cow("Beddie")

my_pets = [my_dog, my_cat, my_cow]

for pet in my_pets:
    pet.make_sound()
