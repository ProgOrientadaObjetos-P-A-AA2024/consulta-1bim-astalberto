class Libro:
    def __init__(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año

    def obtener_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.año}"

libro1 = Libro("1984", "George Orwell", "Ciencia Ficción", 1949)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", 1967)
libro3 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", 1954)

lista_libros = [libro1, libro2, libro3]

print("Información de los libros:")
for libro in lista_libros:
    print(libro.obtener_informacion())