import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class CrearTablas {

    public static void main(String[] args) throws Exception {
        // Cargar el driver JDBC
        Class.forName("org.sqlite.JDBC");

        // Obtener una conexión a la base de datos
        Connection conn = DriverManager.getConnection("jdbc:sqlite:bd_Vehiculo.db");

        // Crear una declaración
        Statement stmt = conn.createStatement();

        // Crear la tabla Vehiculo
        stmt.execute("CREATE TABLE Vehiculo (marca TEXT, modelo TEXT, año INTEGER);");

        // Crear la tabla Empresa
        stmt.execute("CREATE TABLE Empresa (nombre TEXT, direccion TEXT, ruc TEXT);");

        // Cerrar la conexión
        conn.close();
    }
}
