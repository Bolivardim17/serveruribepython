from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

#Llamado a la base para crear tablas
Base=declarative_base()

#Definir los modelos de la base de datos
class Proveedor(Base):
    __tablename__='proveedores'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    documento=Column(String(50))
    direccion=Column(String(100))
    ciudad=Column(String(20))
    representante=Column(String(50))
    telefonoContacto=Column(String(20))
    correo=Column(String(50))
    fechaEnvio=Column(Date)
    costoEnvio=Column(Integer)
    descripcion=Column(String(100))

class Logistica(Base):
    __tablename__='logistica'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    documento=Column(String(50))
    direccion=Column(String(100))
    ciudad=Column(String(20))
    representante=Column(String(50))
    telefonoContacto=Column(String(20))
    correo=Column(String(50))
    fechaEnvio=Column(Date)
    costoEnvio=Column(Integer)
    descripcion=Column(String(100))