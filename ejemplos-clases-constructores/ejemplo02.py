class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}"

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}"
        else:
            return "Fondos insuficientes para realizar el retiro."

    def obtener_saldo(self):
        return f"Saldo actual de la cuenta de {self.titular}: {self.saldo}"

cuenta1 = CuentaBancaria("Juan Pérez", 1000)

print(cuenta1.obtener_saldo())
print(cuenta1.depositar(500))
print(cuenta1.retirar(200))
print(cuenta1.retirar(1500))
