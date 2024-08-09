class Punto: 
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def mostrar(self):
        print(f"Las coordenadas son x = {self.coord_x}, y = {self.coord_y}")

    def mover(self, x_nuevo, y_nuevo):
        self.coord_x = x_nuevo
        self.coord_y = y_nuevo
    
    def calcular_distancia(self, segundo_punto):
        return ((self.coord_x - segundo_punto.coord_x) ** 2 + (self.coord_y - segundo_punto.coord_y) ** 2) ** 0.5

punto_1 = Punto(2, 9)
punto_2 = Punto(3, 6)

punto_1.mostrar()

punto_1.mover(4, 2)
punto_1.mostrar()

distancia = punto_1.calcular_distancia(punto_2)
print(f"La Distancia entre los puntos es: {distancia}")