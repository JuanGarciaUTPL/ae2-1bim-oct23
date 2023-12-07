"""
    Guarda información en las entidades en la base de datos
"""

from bd_Vehiculo import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
marca = "VolksWagen"
modelo = "Amarok"
año = 2020
cadena_vehiculo_sql = """INSERT INTO Vehiculo (marca, modelo, año) \
VALUES ('%s', '%s', %d);""" % (marca, modelo, año)

# ejecutar el SQL
cursor.execute(cadena_vehiculo_sql)

# Crear una cadena que almacene la sentencia de ingreso de información
nombre = "JAG.media"
direccion = "José Joaquín de Olmedo"
ruc = "0987654321"
cadena_empresa_sql = """INSERT INTO Empresa (nombre, direccion, ruc) \
VALUES ('%s', '%s', '%s');""" % (nombre, direccion, ruc)

# ejecutar el SQL
cursor.execute(cadena_empresa_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
