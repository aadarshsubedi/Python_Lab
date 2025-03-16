# Create an abstract base class named "Animal" using Python’s ABC module. 
# The class should have a non abstract method called "move", but it should not have an implementation.
# Then, create four subclasses— "Human," "Snake," "Dog," and "Lion"—that override the "move" method and provide their own specific  
# movement characteristics (e.g., a human walks, a snake slithers, a dog runs, and a lion prowls). 
from abc import ABC, abstractmethod  

class Animal(ABC):
    @abstractmethod
    def move(self):
        """Abstract method without implementation"""
        pass

class Human(Animal):
    def move(self):
        print("A Human walks.")


class Snake(Animal):
    def move(self):
        print("A Snake slithers.")


class Dog(Animal):
    def move(self):
        print("A Dog runs.")


class Lion(Animal):
    def move(self):
        print("A Lion prowls.")


animals = [Human(), Snake(), Dog(), Lion()]
 
for animal in animals:
    animal.move()