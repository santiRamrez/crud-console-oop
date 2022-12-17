from modelo.empleado import Empleado
from dao.dao_empleado import DaoEmpleado
from utils.encoder import Encoder


class EmpleadoDTO:

    def validarLogin(self, username, clave):
        daoempleado = DaoEmpleado()
        resultado = daoempleado.validarLogin(Empleado(correoEmpleado=username, claveEmpleado=Encoder().encode(clave)))
        return True if resultado is not None else None

    def findEmpleado(self, run):
        daoempleado = DaoEmpleado()
        res = daoempleado.findEmpleado(Empleado(runEmpleado=run))
        return res
    
    def addEmpleado(self, run, nombre, apellido, cargo, direccion, clave, correo, comuna):
        daoempleado = DaoEmpleado()
        resultado = daoempleado.addEmpleado(Empleado(runEmpleado=run, nombreEmpleado=nombre, apellidoEmpleado=apellido, cargo=cargo, direccionEmpleado=direccion, claveEmpleado=clave, correoEmpleado=correo, comuna=comuna))
        return resultado

    def updateEmpleado(self, idBD, run, nombre, apellido, cargo, direccion, clave, correo, comuna):
        daoempleado = DaoEmpleado()
        resultado = daoempleado.updateEmpleado(Empleado(idBD=idBD, runEmpleado=run, nombreEmpleado=nombre, apellidoEmpleado=apellido, cargo=cargo, direccionEmpleado=direccion, claveEmpleado=clave, correoEmpleado=correo, comuna=comuna))
        return resultado

    def delEmpleado(self, run):
        daoempleado = DaoEmpleado()
        res = daoempleado.delEmpleado(Empleado(runEmpleado=run))
        return True if res is not None else None
    
    def findEmpleadoByComuna(self, idcomuna):
        daoempleado = DaoEmpleado()
        res = daoempleado.findEmpleadoByComuna(Empleado(comuna=idcomuna))
        return res