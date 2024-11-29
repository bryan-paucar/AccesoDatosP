from datetime import datetime
import peewee
from peewee import MySQLDatabase

# Configura la base de datos
database = MySQLDatabase(
    "hospital",
    host="localhost",
    port=3306,
    user="root",
    password="aludam2",
    autorollback=True,  # Para evitar bloqueos en errores
)

# Define el modelo
class User(peewee.Model):
    username = peewee.CharField(unique=True)
    email = peewee.CharField(index=True)
    created_date = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
        db_table = 'Users'

# Crear la tabla
if __name__ == '__main__':
    database.connect()  # Asegúrate de conectar la base de datos
    database.create_tables([User])  # Crea la tabla sin errores
    print("Tabla 'Users' creada correctamente.")
