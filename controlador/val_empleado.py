# ---- Paquetes de este sistema ----
from controlador.dto_empleado import EmpleadoDTO
from modelo.empleado import Empleado

# ---- Importa funciones de otros objetos ----
from controlador.val_cargo import 



def validarLogin():
    try:
        username = input("Ingrese correo de administrador: ")
        clave = input("Ingrese contraseña: ")
        resultado = EmpleadoDTO().validarLogin(username, clave)
        return True if resultado else None
    except:
        print('Fallo en la validación')

# def findEmpleado(a):
#     identi = int(a)
#     if identi > 0:
#       startDto = EmpleadoDTO()
#       return startDto.findCargo(identi)

def getRecordEmpleado(run):
    data = EmpleadoDTO().findCargo(run)
    return data
 

def addEmpleado():
    try:
        run = input("Por favor ingrese su run: ")
        name = input("Nombre: ")
        lastName = input("Apellido: ")
        cargo = input("Descripción del cargo: ")
        address = input("Dirección: ")
        password = input("Clave: ")
        email = input("Corre electrónico: ")
        comuna = input("Comuna: ")

        if getRecordEmpleado(run):
            print('Ya hay un empleado registrado con ese run :(') 
        else:
            # ----  Add to the database ----
            startDto = EmpleadoDTO()
            #run, nombre, apellido, cargo, direccion, clave, correo, comuna
            print(f'\n{startDto.addEmpleado(run, name, lastName, idcargo, address, password, email, idcomuna)}\n')

    except:
        print('Algo salió mal :( ')   

