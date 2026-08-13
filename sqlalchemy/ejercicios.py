#!/usr/bin/env python3

from datetime import datetime
from typing import List, Annotated
from pydantic import Field, ValidationError, TypeAdapter
from sqlalchemy import create_engine, select, String, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy.exc import IntegrityError

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
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")
    
class Clase(Base):
    __tablename__ = "clases"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150))
    duracion_minutos: Mapped[int] = mapped_column()
    
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped[Curso] = relationship(back_populates="clases")
    
class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(20))
    legajo: Mapped[int] = mapped_column()
    
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")


class Inscripcion(Base):
    __tablename__ = "inscripciones"
        
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime)
    calificacion_final: Mapped[float] = mapped_column()
    
    
    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")
    
    
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
        cur3 = Curso(id=3, titulo="Fisica 1", creditos=16, profesor_id=1)
        cur4 = Curso(id=4, titulo="Estadistica", creditos=31, profesor_id=1)
        cur5 = Curso(id=5, titulo="Laboratorio", creditos=5, profesor_id=1)
        cur6 = Curso(id=6, titulo="Quimica", creditos=22, profesor_id=1)
        cla1 = Clase(id=1, tema="Vectores", duracion_minutos=150, curso_id=1)
        cla2 = Clase(id=2, tema="Funciones", duracion_minutos=120, curso_id=1)
        e1 = Estudiante(id=1, nombre="Carlos", legajo=1234)
        e2 = Estudiante(id=2, nombre="Nicolas", legajo=4321)
        ins1 = Inscripcion(estudiante_id=1, curso_id=1, fecha_inscripcion=datetime(2016, 7, 23), calificacion_final=10)
        ins2 = Inscripcion(estudiante_id=2, curso_id=1, fecha_inscripcion=datetime(2019, 5, 3), calificacion_final=1)
        ins3 = Inscripcion(estudiante_id=1, curso_id=2, fecha_inscripcion=datetime(2021, 2, 23), calificacion_final=4)
        ins4 = Inscripcion(estudiante_id=2, curso_id=2, fecha_inscripcion=datetime(2025, 12, 25), calificacion_final=5)
        session.add_all([dep1, dep2, dep3, p1, p2, p3, cur1, cur2, cur3, cur4, cur5, cur6, cla1, cla2, e1, e2, ins1, ins2, ins3, ins4])
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
        
        profesor_q = "Marcelo"
        stmt_q = select(Curso.titulo, Curso.creditos).join(Profesor).where(Profesor.nombre == profesor_q)
        resultado_q = session.execute(stmt_q).all()
        
        print(f"Cursos que dicta el profesor {profesor_q}:")
        print("Curso | Creditos")
        for fila in resultado_q:
            print(fila)

        estudiante_q = 1234
        stmt_q2 = select(func.avg(Inscripcion.calificacion_final)).join(Estudiante).where(Estudiante.legajo == estudiante_q)
        promedio_q = session.scalar(stmt_q2)
        
        print(f"Promedio de calificaciones del estudiante legajo {estudiante_q}: {promedio_q:.2f}")
        
        stmt_q3 = select(Curso.titulo, func.count()).join(Inscripcion, isouter=True).group_by(Curso.id)
        conteo_q = session.execute(stmt_q3).all()
        
        print("Cantidad de estudiantes anotados:")
        for titulo, cantidad in conteo_q:
            print(f" - {titulo}: {cantidad} alumno(s)")
            
    print("\n\n\n")
    #funcion de negocio
    with Session(engine) as session:
        stmt = select(Estudiante)
        estudiantes = session.scalars(stmt).all()
        stmt = select(Curso)
        cursos = session.scalars(stmt).all()
    
    print("Estudiantes:")
    i=0
    for est in estudiantes:
        i += 1
        print(f"\t{i}) Nombre: {est.nombre}, legajo: {est.legajo}")
    
    validador = TypeAdapter(Annotated[int, Field(ge=1, le=i)])
    
    while True:
        try:
            opcion = input("Ingrese el numero de estudiante a matricular:\n")
            opcion = validador.validate_strings(opcion)
            estudiante = opcion - 1
            break
        except ValidationError:
            print("Ingrese una opcion valida")
            
    print("Cursos:")
    i=0
    for cur in cursos:
        i += 1
        print(f"\t{i}) titulo: {cur.titulo}, id: {cur.id}")
        
    validador2 = TypeAdapter(Annotated[int, Field(ge=1, le=i)])
    
    while True:
        try:
            opcion = input("Ingrese el numero del curso al que se desea inscribir:\n")
            opcion = validador2.validate_strings(opcion)
            curso = opcion - 1
            break
        except ValidationError:
            print("Ingrese una opcion valida")
    
    with Session(engine) as session:
        nueva_inscripcion = Inscripcion(estudiante_id=estudiantes[estudiante].id, curso_id=cursos[curso].id, fecha_inscripcion= func.now(), calificacion_final=0)
        try:
            session.add(nueva_inscripcion)
            session.commit()
            print("Matriculacion exitosa")
        except IntegrityError:
            session.rollback()
            print("El alumno ya esta inscripto en el curso")
        
        stmt = select(Inscripcion).where(Inscripcion.estudiante_id == estudiantes[estudiante].id)
        inscripciones = session.scalars(stmt)
        print("Inscripciones del alumno:")
        for ins in inscripciones:
            print(f"\t{ins.curso.titulo}, fecha de inscripcion: {ins.fecha_inscripcion}")
    

    
    
if __name__ == "__main__":
    main()