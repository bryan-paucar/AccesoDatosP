import cx_Oracle

# Configuración de la conexión
username = 'C##HOSPITAL_DB'
password = 'hospital_db'
dsn = 'localhost/XE'

try:
    # Establecer la conexión
    connection = cx_Oracle.connect(username, password, dsn)
    cursor = connection.cursor()


    # Función para mostrar datos de una tabla
    def fetch_data(table_name):
        print(f"\nConsultando datos en la tabla {table_name}:")
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            if rows:
                print(f"Datos en la tabla {table_name}:")
                for row in rows:
                    print(row)
            else:
                print(f"La tabla {table_name} está vacía.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al consultar la tabla {table_name}: {e}")


    # Consultar y mostrar datos de cada tabla
    tables = ['HOSPITAL', 'SALA', 'PLANTILLA', 'DOCTOR', 'ENFERMO', 'DEPT', 'EMP', 'OCUPACION']
    for table in tables:
        fetch_data(table)

except cx_Oracle.DatabaseError as e:
    print("Hubo un error al conectarse a la base de datos:", e)

finally:
    # Cerrar la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()
