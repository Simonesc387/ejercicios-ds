#!/usr/bin/env python3

from pydantic import BaseModel, Field, HttpUrl, ValidationError
from typing import Annotated, Optional

class PerfilUsuario(BaseModel):
    username: Annotated[str, Field(pattern=r"^[a-z0-9_]{3,20}$")]
    biografia: Annotated[str, Field(max_length=200, default="")]
    redes_sociales: list[str | HttpUrl] | None = None


def main():
    try:
        p1 = PerfilUsuario(username=2)
    except ValidationError as e:
        print(e)
    try:
        p1 = PerfilUsuario(username="as")
    except ValidationError as e:
        print(e)
    try:
        p1 = PerfilUsuario(username="abc123", biografia=2, redes_sociales=12)
    except ValidationError as e:
        print(e)
    try:
        p2 = PerfilUsuario(username="abc123", biografia="Juan", redes_sociales=["Facebook.com", "twitter.com"])
        print(p2)
    except ValidationError as e:
        print(e)
    

if __name__ == "__main__":
    main()