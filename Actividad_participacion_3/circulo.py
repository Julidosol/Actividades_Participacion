import math
class Circulo:
    def __init__ (self, x, y, radio:int):
        self.x = x
        self.y = y
        self.radio = radio 
    def area(self):
        area = (math.pi * (self.radio**2))
        return(area)
    def perimetro(self):
        perimetro = (math.pi * (self.radio + self.radio))
        return(perimetro)
    def pertenece(self, nuevo_x, nuevo_y):
        distancia = math.sqrt((nuevo_x - self.x) ** 2 + (nuevo_y - self.y) ** 2)
        if distancia <= self.radio:
            return ("El punto está en el circulo")
        else:
            return ("El punto no está en el circulo")
        
circulo_1 = Circulo(15, 10, 20)
area = circulo_1.area()
perimetro = circulo_1.perimetro()
print ("El area del circulo es", area)
print("El perimetro del circulo es", perimetro)
print(circulo_1.pertenece(18, 25))