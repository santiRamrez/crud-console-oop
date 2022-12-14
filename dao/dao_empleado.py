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
    
    def findEmpleado(self, empleado):
        sql = "SELECT * FROM empleado WHERE run = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getRunEmpleado(), ))
            result = cursor.fetchone()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result

    def addEmpleado(self, empleado):
        sql = "insert into cargo (idempleado, idcargo, idcomuna, run, nombre, apellido, direccion, clave, correo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (None, empleado.getCargo(), empleado.getComuna(), empleado.getRunEmpleado(), empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getDireccionEmpleado(), empleado.getClaveEmpleado(), empleado.getCorreoEmpleado()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje


