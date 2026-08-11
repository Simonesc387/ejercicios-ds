#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from typing import Annotated, Optional

CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0)]

class Ubicacion(BaseModel):
    longitud: CoordenadaGPS
    latitud: CoordenadaGPS
    etiqueta: Optional[str] = None


def main():
    try:
        u1 = Ubicacion(longitud=123, latitud=12)
    except ValidationError as e:
        print(e)
    try:
        u2 = Ubicacion(longitud=12, latitud=123, etiqueta=3)
    except ValidationError as e:
        print(e)
    try:
        u3 = Ubicacion(longitud=89.0, latitud=-30.9, etiqueta="abc")
        print(u3)
    except ValidationError as e:
        print(e)
    

if __name__ == "__main__":
    main()