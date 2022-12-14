from modelo.empleado import Empleado
from dao.dao_empleado import DaoEmpleado
from utils.encoder import Encoder


class EmpleadoDTO:

    def validarLogin(self, username, clave):
        daoempleado = DaoEmpleado()
        resultado = daoempleado.validarLogin(Empleado(correoEmpleado=username, claveEmpleado=Encoder().encode(clave)))
        return True if resultado is not None else None
    
