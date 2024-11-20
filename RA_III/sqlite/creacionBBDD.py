from peewee import *

# Conectar o crear la base de datos SQLite "people.db"
db = SqliteDatabase('people.db')

# Modelo "Person"
class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # Usar la base de datos "people.db"

# Modelo "Pet"
class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')  # Relación con "Person"
    name = CharField()                               # Nombre de la mascota
    animal_type = CharField()                        # Tipo de animal (perro, gato, etc.)

    class Meta:
        database = db  # Usar la base de datos "people.db"

# Conectar y crear tablas
db.connect()
db.create_tables([Person, Pet])  # Asegurarse de crear las tablas

print("Tablas 'Person' y 'Pet' creadas con éxito.")

# Insertar ejemplos
# Crear un propietario
person = Person.create(name="Alice", birthday="1992-07-15")

# Crear mascotas para este propietario
Pet.create(owner=person, name="Fido", animal_type="dog")
Pet.create(owner=person, name="Whiskers", animal_type="cat")

print("Datos de ejemplo añadidos a la base de datos.")
