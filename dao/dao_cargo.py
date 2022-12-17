from conex import conn
import traceback

class DaoCargo:
    def __init__(self):
        try:
            self.conn = conn.Conex('localhost', 'root', 'mlkihad1969', 'minimarket')
        except Exception as ex:
            print(ex)

# ---- Getter ----

    def getConex(self):
        return self.conn

# ---- Methods ----

    def addCargo(self, cargo):
        sql = "insert into cargo (idcargo, numerocargo, nombrecargo) values (%s, %s, %s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (None, cargo.getIdCargo(), cargo.getDescripcionCargo()))
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


    def findCargo(self, cargo):
        sql = "SELECT * FROM cargo WHERE numerocargo = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdCargo(), ))
            result = cursor.fetchone()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result


    def updateCargo(self, cargo):
        sql = "UPDATE cargo SET nombrecargo = %s WHERE numerocargo = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getDescripcionCargo(), cargo.getIdCargo()))
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


    def delCargo(self, cargo):
        sql = "DELETE FROM cargo WHERE numerocargo = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdCargo(), ))
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


    def findAllCargo(self):
        sql = "SELECT * FROM cargo"
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


    def getRecordByName(self, cargo):
        sql = "SELECT * FROM cargo WHERE nombrecargo = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getDescripcionCargo(), ))
            result = cursor.fetchone()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result
    
    def getRecordByID(self, id):
        sql = "SELECT * FROM cargo WHERE idcargo = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (id, ))
            result = cursor.fetchone()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result

