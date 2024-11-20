from peewee import IntegrityError
from CreacionTablaPeewee import User, database  # Importamos User y la conexión

class GestorUsuarios:
    """Clase para manejar la inserción de usuarios en la tabla Users."""

    @staticmethod
    def add_user(username, email):
        """Inserta un nuevo usuario en la tabla Users."""
        try:
            with database.atomic():  # Transacción para garantizar consistencia
                new_user = User.create(username=username, email=email)
                print(f"Usuario agregado: {new_user.username} - {new_user.email}")
        except IntegrityError:
            print(f"Error: El usuario '{username}' ya existe en la base de datos.")

# Ejecución del código: agregar usuarios
if __name__ == "__main__":
    # Conectar a la base de datos
    database.connect()

    # Lista de usuarios a agregar
    usuarios = [
        {"username": "johndoe", "email": "johndoe@example.com"},
        {"username": "janedoe", "email": "janedoe@example.com"},
        {"username": "alexsmith", "email": "alexsmith@example.com"}
    ]

    # Agregar usuarios usando la clase GestorUsuarios
    for usuario in usuarios:
        GestorUsuarios.add_user(usuario["username"], usuario["email"])