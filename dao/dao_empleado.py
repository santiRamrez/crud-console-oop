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
        sql = "insert into empleado (idcargo, idcomuna, run, nombre, apellido, direccion, clave, correo) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getCargo(), empleado.getComuna(), empleado.getRunEmpleado(), empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getDireccionEmpleado(), empleado.getClaveEmpleado(), empleado.getCorreoEmpleado()))
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
    
    def updateEmpleado(self, emp):
        sql = "UPDATE empleado SET "
        endsql = " WHERE idempleado = %s"
        newsql = ''
        listValues = []
        values = ''
        # Concatenaciones para validar y armar la query
        if emp.getRunEmpleado():
            string = "run = %s,"
            sql = sql + string
            listValues.append(emp.getRunEmpleado())

        if emp.getNombreEmpleado():
            string = " nombre = %s,"
            sql = sql + string
            listValues.append(emp.getNombreEmpleado())
        
        if emp.getApellidoEmpleado():
            string = " apellido = %s,"
            sql = sql + string 
            listValues.append(emp.getApellidoEmpleado())
        
        if emp.getCargo():
            string = " idcargo = %s,"
            sql = sql + string
            listValues.append(emp.getCargo())

        if emp.getDireccionEmpleado():
            string = " direccion = %s,"
            sql = sql + string 
            listValues.append(emp.getDireccionEmpleado())
        
        if emp.getClaveEmpleado():
            string = " clave = %s,"
            sql = sql + string 
            listValues.append(emp.getClaveEmpleado())
        
        if emp.getCorreoEmpleado():
            string = " correo = %s,"
            sql = sql + string 
            listValues.append(emp.getCorreoEmpleado())
        
        if emp.getComuna():
            string = " idcomuna = %s,"
            sql = sql + string 
            listValues.append(emp.getComuna())
        
        
        #Delete the last comma of the sets
        newsql = sql[0:len(sql)-1]
        #Concatenate and close the query
        newsql = newsql + endsql
        listValues.append(emp.getId())
        #Convert to a tuple
        values = tuple(listValues)
            

        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            #Pass values of the list in order dinamically
            cursor.execute(newsql, values)
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                # mensaje="No se realizaron cambios"
                mensaje = f'Query: {newsql} \nValues: {values}'
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def delEmpleado(self, emp):
        sql = "DELETE FROM empleado WHERE run = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (emp.getRunEmpleado(), ))
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

    def findEmpleadoByComuna(self, emp):
        sql = "SELECT * FROM EMPLEADO WHERE idcomuna = %s;"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (emp.getComuna(), ))
            result = cursor.fetchall()
            
        except Exception as ex:
            print(traceback.print_exc())

        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result
    



