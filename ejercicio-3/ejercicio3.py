#!/usr/bin/env python3

def main():
    try:
        costoPasaje = float(input("Ingrese el costo del pasaje:"))
        costoNoche = float(input("Ingrese el costo por noche del alojamiento:"))
        cantNoche = int(input("Ingrese la cantidad de noches:"))
        dinero = float(input("Ingrese el dinero que tiene disponible:"))
        costoTotal = (costoPasaje*2)+(costoNoche*cantNoche)
        viajePosible = (dinero>=costoTotal)
        if viajePosible:
            print(f"Es posible realizar el viaje con la cantidad de dinero. Costo total {costoTotal}")
        else:
            print(f"No es posible realizar el viaje con la cantidad de dinero. Costo total {costoTotal}")
    except ValueError:
        print("Ingrese un numero valido")


if __name__ == "__main__":
    main()