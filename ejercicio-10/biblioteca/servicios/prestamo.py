from biblioteca.modelos.libro import Libro 

def realizarPrestamo(Libro):
    if Libro.disponibilidad == True:
        Libro.disponibilidad = False
        print(f"El libro {Libro.titulo} (isbn: {Libro.isbn}) ha sido prestado con exito.")
    else:
        print(f"El libro {Libro.titulo} (isbn: {Libro.isbn}) no se encuentra disponible.")

def realizarDevolucion(Libro):
    if Libro.disponibilidad == True:
        print(f"El libro {Libro.titulo} (isbn: {Libro.isbn}) ya se encontraba en la biblioteca.")
    else:
        Libro.disponibilidad = True
        print(f"El libro {Libro.titulo} (isbn: {Libro.isbn}) ha sido devuelto con exito.")

def consultarDisponibilidad(Libro):
    if Libro.disponibilidad == True:
        print(f"El libro {Libro.titulo} (isbn: {Libro.isbn}) se encuentra en la biblioteca.")
    else:
        print(f"El libro {Libro.titulo} (isbn: {Libro.isbn}) no se encuentra en la biblioteca.")

