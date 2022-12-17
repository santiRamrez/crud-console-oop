from conex import conn
import traceback

class DaoComuna:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "mlkihad1969", "minimarket")
        except Exception as ex:
            print(ex)

# ---- Getter ----

    def getConex(self):
        return self.conn

# ---- Methods ----

    def addComuna(self, comuna):
        sql = "insert into comuna (idcomuna, numerocomuna, nombrecomuna) values (%s, %s, %s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (None, comuna.getIdComuna(), comuna.getDescripcionComuna()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente "
            else:
                mensaje="No se pudo agregar el registro "
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos... vuelva a intentarlo "
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje


    def findComuna(self, comuna):
        sql = "SELECT * FROM comuna WHERE numerocomuna = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.getIdComuna(), ))
            result = cursor.fetchone()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result


    def updateComuna(self, comuna):
        sql = "UPDATE comuna SET nombrecomuna = %s WHERE numerocomuna = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.getDescripcionComuna(), comuna.getIdComuna()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Los Datos de la Comuna han sido modificados"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje


    def delComuna(self, comuna):
        sql = "DELETE FROM comuna WHERE numerocomuna = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.getIdComuna(), ))
            c.getConex().commit()
            str = cursor.statement
            if str:
                mensaje = str
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje


    def findAllComuna(self):
        sql = "SELECT * FROM comuna"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result


    def getRecordByName(self, comuna):
        sql = "SELECT * FROM comuna WHERE nombrecomuna = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.getDescripcionComuna(), ))
            result = cursor.fetchone()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result