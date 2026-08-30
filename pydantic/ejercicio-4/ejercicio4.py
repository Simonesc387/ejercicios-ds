#!/usr/bin/env python3

from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import Annotated

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: Annotated[int, Field(ge=1, le=5)]


def main():
    try:
        u1 = UsuarioSistema(email="Pablo", nivel_acceso=32)
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()