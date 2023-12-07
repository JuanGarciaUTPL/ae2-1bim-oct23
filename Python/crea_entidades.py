from bd_Vehiculo import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una tabla denominada Vehiculo

cadena_vehiculo_sql = 'CREATE TABLE Vehiculo (marca TEXT, modelo TEXT, año INTEGER)'

# ejecutar el SQL
cursor.execute(cadena_vehiculo_sql)

cadena_empresa_sql = 'CREATE TABLE Empresa (nombre TEXT, direccion TEXT, ruc TEXT)'

# ejecutar el SQL
cursor.execute(cadena_empresa_sql)

# cerrar la enlace a la base de datos (recomendado)
cursor.close()
