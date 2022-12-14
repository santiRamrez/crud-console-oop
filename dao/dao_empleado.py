from conex import conn
import traceback

class DaoEmpleado:
    def __init__(self):
        try:
            self.conn = conn.Conex('localhost', 'root', 'mlkihad1969', 'minimarket')
        except Exception as ex:
            print(ex)

# ---- Getter ----
    def getConex(self):
        return self.conn

# ---- Methods ----
    def validarLogin(self, empleado):
        sql = "select correo from empleado where correo = %s and clave = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getCorreoEmpleado(), empleado.getClaveEmpleado()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    


