#!/usr/bin/env python3

def suma(cantidad):
    resultado = 0
    for i in range(cantidad+1):
        resultado += i
    print(f"\nLa suma de los primeros {cantidad} numeros naturales es: {resultado}\n")

def rango(inicio, final):
    total = 0
    print(f"Numeros divisibles por 3 dentro del rango {inicio}-{final}:")
    for i in range(inicio, final+1):
        if ((i % 3)==0):
            print(f"{i}")
            total +=1
    if total>0:
        print(f"\nTotal: {total} numeros\n")
    else:
        print("\nNo se encontraron numeros divisibles por 3 dentro del rango\n")

def main():
    while True:
        while True:
            try:
                opcion = int(input("Ingrese la operacion que desea realizar:̣\n\t1. Calcular la suma de los primeros N numeros naturales.\n\t2. Encontrar todos los números divisibles por 3 en un rango dado\n\t3. Salir\n"))
                if opcion in range(1,4):
                    break
                else:
                    print("Ingrese una opcion valida.\n")
            except ValueError:
                print("Ingrese una opcion valida.\n")
        match opcion:
            case 1:
                while True:
                    try:
                        cant = int(input("\nIngrese la cantidad de enteros a sumar: "))
                        if cant >= 0:
                            break
                        else:
                            print("Ingrese una cantidad valida.\n")
                    except ValueError:
                        print("Ingrese una cantidad valida.\n")
                suma(cant)
            case 2:
                while True:
                    try:
                        inicio = int(input("\nIngrese el inicio: "))
                        final = int(input("Ingrese el final: "))
                        if inicio > final:
                            print("Ingrese valores validos.\n")
                        else:
                            break
                    except ValueError:
                        print("Ingrese valores validos.\n")
                rango(inicio, final)
            case 3:
                break


if __name__ == "__main__":
    main()