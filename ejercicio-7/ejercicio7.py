#!/usr/bin/env python3

def analizar_temperaturas(registros):
    minimo = min(registros)
    maximo = max(registros)
    promedio = sum(registros)/len(registros)
    return minimo, maximo, promedio


def main():
    temperaturas = [12, 41, 25, 44, 32, 9, 19, 28, 34, 16]
    tempMin, tempMax, tempProm = analizar_temperaturas(temperaturas)
    print(f"Temperaturas: {temperaturas}")
    print(f"Temperatura minima: {tempMin}")
    print(f"Temperatura maxima: {tempMax}")
    print(f"Temperatura promedio: {tempProm}")


if __name__ == "__main__":
    main()