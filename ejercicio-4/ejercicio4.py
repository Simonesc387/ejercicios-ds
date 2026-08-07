#!/usr/bin/env python3

def conversionC(tempF):
    resultado = (tempF-32)/1.8
    print(f"La temperatura {tempF}°F en celsius es: {resultado}°C")

def conversionF(tempC):
    resultado = (tempC*1.8)+32
    print(f"La temperatura {tempC}°C en Farenheit es: {resultado}°F")

def main():
    try:
        temperatura = float(input("Ingrese la temperatura:"))
        escala = input("Ingrese la escala utilizada:")
        if escala.lower() == "celsius":
            conversionF(temperatura)
        else:
            conversionC(temperatura)
    except ValueError:
        print("Ingrese un numero valido")


if __name__ == "__main__":
    main()