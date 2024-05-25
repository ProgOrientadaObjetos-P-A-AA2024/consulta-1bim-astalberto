frutas = ["manzana", "banana", "cereza"]
bandera = True

while bandera:
    aux = input("Ingrese fruta (o 'salir' para terminar): ")
    if aux.lower() == 'salir':
        bandera = False
    else:
        frutas.append(aux)

print("Lista de frutas:", frutas)


if len(frutas) > 1:
    print("Segunda fruta en la lista:", frutas[1])
else:
    print("No hay suficientes frutas en la lista para acceder al segundo elemento.")

bandera = True

while bandera:
    aux = input("Ingrese fruta a eliminar (o 'salir' para terminar): ")
    if aux.lower() == 'salir':
        bandera = False
    elif aux in frutas:
       frutas.remove(aux)
       print("Fruta eliminada:", aux)
    else:
        print("La fruta no está en la lista.")
    

    print("Lista de frutas actualizada:", frutas)
