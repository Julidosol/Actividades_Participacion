class Rectangulo:
    def __init__(self, x_1:int, y_1:int, x_2:int, y_2:int):
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2

    def base(self):
        return self.x_2 - self.x_1
    
    def altura(self):
        return self.y_2 - self.y_1
    
    def perimetro(self): 
        return 2*(self.base() + self.altura()) 
    
    def area(self):
        return (self.base() * self.altura())
    
    def cuadrado(self):
        if self.base() == self.altura():
            return("El rectangulo es Cuadrado")
        else:
            return("El rectangulo no es cuadrado")

Rectangulo_1 = Rectangulo(1, 2, 4, 6)
perimetro = Rectangulo_1.perimetro()
area = Rectangulo_1.area()

print("El perimetro del rectangulo es: ", perimetro)
print("el area del rectangulo es: ", area)
print(Rectangulo_1.cuadrado())