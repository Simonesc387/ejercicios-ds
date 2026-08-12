#!/usr/bin/env python3

from datetime import datetime
from typing import List
from sqlalchemy import create_engine, select, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine("sqlite://", echo=False)

class Base(DeclarativeBase):
    pass
    
class Departamento(Base):
    __tablename__ = "departamentos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    profesores: Mapped[List["Profesor"]] = relationship(back_populates="departamento")

class Profesor(Base):
    __tablename__ = "profesores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(20))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    
    departamento: Mapped[Departamento] = relationship(back_populates="profesores")
    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")
    
class Curso(Base):
    __tablename__ = "cursos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column()
    
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped[Profesor] = relationship(back_populates="cursos")
    clases: Mapped[List["Clase"]] = relationship(back_populates="curso")
    
class Clase(Base):
    __tablename__ = "clases"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150))
    duracion_minutos: Mapped[int] = mapped_column()
    
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped[Curso] = relationship(back_populates="clases")
    
def main():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        dep1 = Departamento(id=1, nombre="Matematica")
        dep2 = Departamento(id=2, nombre="Ingenieria")
        dep3 = Departamento(id=3, nombre="Economia")
        p1 = Profesor(id=1, nombre="Marcelo", email="marcelo@gmail.com", fecha_ingreso=datetime(2010, 2, 23), departamento_id=1)
        p2 = Profesor(id=2, nombre="Jose", email="jose@gmail.com", fecha_ingreso=datetime(2019, 10, 31), departamento_id=1)
        p3 = Profesor(id=3, nombre="Juan", email="juan@gmail.com", fecha_ingreso=datetime(2014, 8, 1), departamento_id=1)
        cur1 = Curso(id=1, titulo="Algebra 1", creditos=10, profesor_id=1)
        cur2 = Curso(id=2, titulo="Analisis 1", creditos=15, profesor_id=2)
        cla1 = Clase(id=1, tema="Vectores", duracion_minutos=150, curso_id=1)
        cla2 = Clase(id=2, tema="Funciones", duracion_minutos=120, curso_id=1)
        session.add(dep1)
        session.add(dep2)
        session.add(dep3)
        session.add(p1)
        session.add(p2)
        session.add(p3)
        session.add(cur1)
        session.add(cur2)
        session.add(cla1)
        session.add(cla2)
        session.commit()
        
    with Session(engine) as session:
        stmt = select(Departamento)
        departamentos = session.scalars(stmt)
        for dep in departamentos:
            print(f"departamento: {dep.nombre}, profesores:")
            for prof in dep.profesores:
                print(prof.nombre)
        stmt = select(Profesor)
        profesores = session.scalars(stmt)
        for prof in profesores:
            print(f"Profesor: {prof.nombre}, email: {prof.email}, fecha de ingreso: {prof.fecha_ingreso}, departamento: {prof.departamento.nombre}, cursos:")
            for cur in prof.cursos:
                print(cur.titulo)
        stmt = select(Curso)
        cursos = session.scalars(stmt)
        for cur in cursos:
            print(f"Curso: {cur.titulo}, creditos: {cur.creditos}, profesor: {cur.profesor.nombre}")
        stmt = select(Curso).where(Curso.id==1)
        curso = session.scalars(stmt).first()
        clases = curso.clases
        print(f"Clases del curso {curso.titulo}:")
        for cla in clases:
            print(f"\ttema: {cla.tema}, duracion(minutos): {cla.duracion_minutos}")
    
    
    
if __name__ == "__main__":
    main()