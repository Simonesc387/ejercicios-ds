#!/usr/bin/env python3


def main():
    PASSW = "Admin1234"
    intentos = 0
    while intentos < 3:
        password = input("Ingrese el password: ")
        if password==PASSW:
            print("Password correcto")
            break
        else:
            intentos += 1
            print(f"Password incorrecto. Intente nuevamente.(Intentos restantes {3 - intentos})")
    if intentos == 3:
        print("Ha alcanzado la cantidad maxima de intentos.")


if __name__ == "__main__":
    main()