from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def laturi(self):
        pass

class Triunghi(Polygon):
    def laturi(self):
        print("Triunghiul are 3 laturi")

class Patrat(Polygon):
    def laturi(self):
        print("Patratul are 4 laturi")

class Hexagon(Polygon):
    def laturi(self):
        print("Hexagonul are 6 laturi")

triung = Triunghi()
triung.laturi()
patrat = Patrat()
patrat.laturi()
hexag = Hexagon()
hexag.laturi()