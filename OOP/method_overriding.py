from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self, sound):
        return sound


class Dog(Animal):
    def make_sound(self):
        return super().make_sound("Bark!")


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())
