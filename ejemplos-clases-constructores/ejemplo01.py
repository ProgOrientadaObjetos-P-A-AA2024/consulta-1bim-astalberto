class Computador:
    def __init__(self, procesador, marca, ram, almacenamiento):
        self.procesador = procesador
        self.marca = marca
        self.ram = ram
        self.almacenamiento = almacenamiento

    def presentar(self):
        return f"El Computador tiene las siguientes características:\nProcesador: {self.procesador}\nMarca: {self.marca}\nRam: {self.ram} GB\nAlmacenamiento: {self.almacenamiento} TB\n"

computador01 = Computador("Intel i7", "Lenovo", 16, 1)

print(computador01.presentar())
