#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy import create_engine, select, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(20))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    
def main():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        p1 = Profesor(id=1, nombre="Marcelo", email="marcelo@gmail.com", fecha_ingreso=datetime(2010, 2, 23))
        p2 = Profesor(id=2, nombre="Jose", email="jose@gmail.com", fecha_ingreso=datetime(2019, 10, 31))
        p3 = Profesor(id=3, nombre="Juan", email="juan@gmail.com", fecha_ingreso=datetime(2014, 8, 1))
        session.add(p1)
        session.add(p2)
        session.add(p3)
        session.commit()
        
    with Session(engine) as session:
        stmt = select(Profesor)
        profesores = session.scalars(stmt)
        for prof in profesores:
            print(f"Profesor: {prof.nombre}, email: {prof.email}, fecha de ingreso: {prof.fecha_ingreso}")
    
    
    
if __name__ == "__main__":
    main()