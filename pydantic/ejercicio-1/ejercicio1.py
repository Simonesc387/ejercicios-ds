#!/usr/bin/env python3

from pydantic import BaseModel, Field, EmailStr, PositiveInt, ValidationError
from typing import Annotated
class Estudiante(BaseModel):
    legajo: PositiveInt
    nombre_completo: Annotated[str, Field(min_length=5)]
    email: EmailStr
    promedio: Annotated[float, Field(default=0.0, ge=0.0, le=10.0)]


def main():
    try:
        e1 = Estudiante(legajo=-123, nombre_completo="Pablo", email="Pablo@google.com", promedio=5.0)
    except ValidationError as e:
        print(e)
    try:
        e2 = Estudiante(legajo=123, nombre_completo="Juan", email="Pablo@google.com", promedio=5.0)
    except ValidationError as e:
        print(e)
    try:
        e3 = Estudiante(legajo=123, nombre_completo="Pablo", email="Pablo", promedio=5.0)
    except ValidationError as e:
        print(e)
    try:
        e4 = Estudiante(legajo=123, nombre_completo="Pablo", email="Pablo@google.com", promedio=50.0)
    except ValidationError as e:
        print(e)
    try:
        e5 = Estudiante(legajo=123, nombre_completo="Pablo", email="Pablo@google.com", promedio=5.0)
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()