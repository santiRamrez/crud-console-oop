# ---- Paquetes de este sistema ----
from controlador.dto_empleado import EmpleadoDTO
# from modelo.empleado import Empleado

def validarLogin():
    try:
        username = input("Ingrese correo de administrador: ")
        clave = input("Ingrese contraseña: ")
        resultado = EmpleadoDTO().validarLogin(username, clave)
        return True if resultado else None
    except:
        print('Fallo en la validación')


    