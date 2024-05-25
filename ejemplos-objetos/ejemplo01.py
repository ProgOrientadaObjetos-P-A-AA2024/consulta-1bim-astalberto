class Automovil:
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.encendido = False

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Año: {self.año}"

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.marca} {self.modelo} arrancó."
        else:
            return f"El {self.marca} {self.modelo} ya está en marcha."

    def detener(self):
        if self.encendido:
            self.encendido = False
            return f"El {self.marca} {self.modelo} se detuvo."
        else:
            return f"El {self.marca} {self.modelo} ya está detenido."

automovil1 = Automovil("Toyota", "Corolla", "Rojo", 2020)
automovil2 = Automovil("Ford", "Mustang", "Negro", 2018)

print("Información del automóvil 1:")
print(automovil1.obtener_informacion())
print("Información del automóvil 2:")
print(automovil2.obtener_informacion())


aux1 = int(input("Seleccione su auto (1 o 2): ")) - 1

if aux1 == 0:
    print("Presione 1 para arrancar el auto")
    aux2 = int(input())
    while aux2 == 1:
        print(automovil1.arrancar())
        aux2 = int(input("Si desea detener el auto presione 0: "))
        if aux2 == 0:
            print(automovil1.detener())
            break

elif aux1 == 1:
    print("Presione 1 para arrancar el auto")
    aux2 = int(input())
    while aux2 == 1:
        print(automovil2.arrancar())
        aux2 = int(input("Si desea detener el auto presione 0: "))
        if aux2 == 0:
            print(automovil2.detener())
            break
