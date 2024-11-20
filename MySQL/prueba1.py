import mysql.connector as bd

bd_conexion = bd.connect(
    host='localhost',
    port='3306',
    user='prueba1',
    password='prueba1',
    database='prueba1'
)
cursor = bd_conexion.cursor()
try:
    cursor.execute("SELECT Codalumno, Nombre, Direccion, Localidad from alumno")

    for cod, nomb, dir, loc in cursor:
        print("Código alumno: ",cod)
        print("Nombre: ",nomb)
        print("Dirección: ",dir)
        print("Localidad: ",loc)

except bd.Error as error:
    print("Error: ",error)
bd_conexion.close()