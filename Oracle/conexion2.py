import cx_Oracle

# Configuración de la conexión
username = 'C##HOSPITAL_DB'
password = 'hospital_db'
dsn = 'localhost/XE'

try:
    # Establecer la conexión
    connection = cx_Oracle.connect(username, password, dsn)
    cursor = connection.cursor()

    # Consulta para contar las filas en una tabla como prueba
    cursor.execute("SELECT COUNT(*) FROM HOSPITAL")
    count = cursor.fetchone()[0]
    print(f"Número de filas en la tabla HOSPITAL: {count}")

except cx_Oracle.DatabaseError as e:
    print("Hubo un error al conectarse a la base de datos:", e)

finally:
    # Cerrar la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()
