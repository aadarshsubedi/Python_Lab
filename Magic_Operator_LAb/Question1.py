#Create an abstract base class named "Polygon" using Python’s ABC module.
# The class should have an abstract  method called "noofsides", which must be implemented by its subclasses. 
# Then, create four subclasses— "Triangle," "Pentagon," "Hexagon," and "Quadrilateral"
# —that inherit from "Polygon" and override the  "noofsides" method to print the number of sides each shape has. 
from abc import ABC, abstractmethod  

class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Triangle(Polygon):
    def no_of_sides(self):
        print("Triangle has 3 sides.")


class Quadrilateral(Polygon):
    def no_of_sides(self):
        print("Quadrilateral has 4 sides.")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("Pentagon has 5 sides.")


class Hexagon(Polygon):
    def no_of_sides(self):
        print("Hexagon has 6 sides.")


shapes = [Triangle(), Quadrilateral(), Pentagon(), Hexagon()]

for shape in shapes:
    shape.no_of_sides()