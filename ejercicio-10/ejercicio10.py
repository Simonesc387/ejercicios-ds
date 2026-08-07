#!/usr/bin/env python3

from biblioteca.modelos.libro import Libro
from biblioteca.servicios.prestamo import realizarDevolucion, realizarPrestamo, consultarDisponibilidad

def main():
    l1 = Libro("Hola","Juan",1234)
    l2 = Libro("Chau","Jose",4321)
    realizarDevolucion(l1)
    realizarPrestamo(l2)
    realizarPrestamo(l1)
    realizarPrestamo(l2)
    realizarDevolucion(l2)
    consultarDisponibilidad(l1)
    consultarDisponibilidad(l2)


if __name__ == "__main__":
    main()