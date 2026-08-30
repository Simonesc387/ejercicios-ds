#!/usr/bin/env python3

from pydantic import BaseModel, ValidationError
from typing import Union, Literal

TIPO = Literal["sensor", "actuador", "gateway"]

class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: TIPO


def main():
    try:
        d1 = Dispositivo(id_dispositivo=123, tipo="sensor")
    except ValidationError as e:
        print(e)
    try:
        d2 = Dispositivo(id_dispositivo="123abc", tipo="actuador")
    except ValidationError as e:
        print(e)
    try:
        d3 = Dispositivo(id_dispositivo=0.5, tipo="gateway")
    except ValidationError as e:
        print(e)
    try:
        d4 = Dispositivo(id_dispositivo=1, tipo="abc")
    except ValidationError as e:
        print(e)
    

if __name__ == "__main__":
    main()