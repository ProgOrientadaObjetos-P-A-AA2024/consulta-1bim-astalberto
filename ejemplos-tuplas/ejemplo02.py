colores = ("rojo", "verde", "azul")

print("Primer color:", colores[0])
print("Último color:", colores[-1])

print("Todos los colores:")
for color in colores:
    print(color)

aux=print("Color a buscar")
# Comprobar si un color está en la tupla
if aux in colores:
    print("El color esta en la lista")
