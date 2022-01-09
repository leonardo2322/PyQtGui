import psycopg2 as pg
from data import conection
name = ""
passwor= ""
try:
    with conection.cursor() as cursor:
        query = """INSERT INTO Usuarios(usuario, passw) VALUES (%s,%s) """
        cursor.execute(query, name,passwor)
        conection.commit()

except pg.Error as e:
    print("error de conexion",e)
finally:
    conection.close()