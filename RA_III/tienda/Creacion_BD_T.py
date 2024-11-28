from peewee import *

#Conectar o crear la base de datos SQLite "tienda.db"
db = SqliteDatabase('tienda.db')

#Modelo "Cliente"
class Cliente(Model):
    codigo_cli = IntegerField
    nombre = CharField
    localidad = CharField
    tlf = CharField

#Modelo "Proveedore"
class Proveedor(Model):
    codigo_prov = IntegerField
    nombre = CharField
    localidad = CharField
    fecha_alta = DateField
    comision = FloatField

#Modelo "Articulo"
class Articulo(Model):
    codigo_art
    denominacion
    precio
    stock
    zona
    codigo_prov



