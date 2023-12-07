import java.sql.Connection;
import java.sql.DriverManager;

public class CrearBD {

    public static void main(String[] args) throws Exception {
        // Cargar el driver JDBC
        Class.forName("org.sqlite.JDBC");

        // Obtener una conexión a la base de datos
        Connection conn = DriverManager.getConnection("jdbc:sqlite:bd_Vehiculo.db");

        // Cerrar la conexión
        conn.close();
    }
}
