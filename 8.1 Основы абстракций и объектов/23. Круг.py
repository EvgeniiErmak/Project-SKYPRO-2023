import math

class Circle:

    def __init__(self, radius):
        self.radius = radius


    def get_radius(self):
        return self.radius


    def get_diameter(self):
        return self.get_radius() * 2


    def get_perimeter(self):
        return self.get_diameter() * math.pi # math.pi это pi=3.14

# Не удаляйте этот код, он нужен для проверки

circle_1 = Circle(7)
print("радиус", circle_1.get_radius() )
print("диаметр", circle_1.get_diameter() )
print("периметр", round(circle_1.get_perimeter(),1))