from conex import conn
import traceback

class daoUser:
    def __init__(self):
        try:
            self.conn = conn.Conex('Localhost', 'root', 'mlkihad1969', 'minimarket')
        except Exception as ex:
            print(ex)

# ---- Getter ----
    def getConex(self):
        return self.conn

# ---- Methods ----

    def listarUsuarios(self):

        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select username, email, password, create_time from users")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result

    def buscarUsuario(self, user):
        sql = "select username, email, password create_time from users where username = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.username,))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def validarLogin(self,user):
        sql = "select username from users where username = %s and password = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.username, user.password))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    def actualizarUsuario(self, user):
        sql = "update users set email=%s, password = %s where username = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.email, user.password, user.username))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    def agregarUsuario(self,user):
        sql = "insert into users (username, email, password, create_time) values (%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.username,user.email, user.password,user.create_time))
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



