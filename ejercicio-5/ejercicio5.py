#!/usr/bin/env python3


def main():
    password = input("Ingrese el password (Debe contener al menos 8 caracteres, una mayuscula y una minuscula):")
    if len(password)<8:
        print("El password debe contener al menos 8 caracteres.")
    elif password.islower():
        print("El password debe contener al menos una mayuscula.")
    elif password.isupper():
        print("El password debe contener al menos una minuscula.")
    else:
        print("El password contiene los requerimientos necesarios.")


if __name__ == "__main__":
    main()