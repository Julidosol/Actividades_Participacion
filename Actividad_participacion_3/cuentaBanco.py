class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def mostrar_informacion(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {self.propietarios}")
        print(f"Balance: {self.balance}")

    def depositar(self, cantidad):
            print(f"Depósito exitoso. Nuevo balance: {self.balance}")
    
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se ha aplicado una cuota de manejo de 2%. Nuevo balance: {self.balance}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {self.propietarios}")
        print(f"Balance: {self.balance}")

cuenta = CuentaBancaria("123456789", "Julian Osorio", 1000.0)

cuenta.mostrar_detalles()

cuenta.depositar(500)

cuenta.aplicar_cuota_manejo()

cuenta.mostrar_detalles()