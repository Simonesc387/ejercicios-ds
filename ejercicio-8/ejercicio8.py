#!/usr/bin/env python3

def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip = False):
    if ((precio_base < 0) or (porcentaje_descuento < 0) or (porcentaje_descuento > 100)):
        raise ValueError
    descuento = precio_base*(1-porcentaje_descuento/100)
    print(f"precio: {precio_base}, descuento: {porcentaje_descuento}, vip:{es_vip}, total antes de descuento vip: {descuento}")
    if es_vip:
        return descuento*0.95
    else:
        return descuento


def main():
    try:
        print(calcular_precio_final(-20, 5, True))
    except ValueError:
        print("valor invalido")

    try:
        print(calcular_precio_final(13, -45, True))
    except ValueError:
        print("valor invalido")
    print(calcular_precio_final(100))
    print(calcular_precio_final(100, 40))
    print(calcular_precio_final(100, 45, True))
    try:
        print(calcular_precio_final(13, 300, True))
    except ValueError:
        print("valor invalido")


if __name__ == "__main__":
    main()