# ---- Paquetes de este sistema ----
from controlador.dto_empleado import EmpleadoDTO
from modelo.empleado import Empleado

# ---- Importa funciones de otros objetos ----
from controlador.val_cargo import getCargoRecordByName
from controlador.val_cargo import findAllCargo
from controlador.val_cargo import getRecordByID_Cargo # ---- It needs at pk and return a tuple with the record from dB

from controlador.val_comuna import getComunaRecordByName
from controlador.val_comuna import findAllComuna
from controlador.val_comuna import getRecordByID_Comuna #--- It needs at pk and return a tuple with the record from dB

def valNoEmpty(b):
    a = input(b)
    if len(a) > 0:
        return a

def validarLogin():
    try:
        username = input("Ingrese correo de administrador: ")
        clave = input("Ingrese contraseña: ")
        resultado = EmpleadoDTO().validarLogin(username, clave)
        return True if resultado else None
    except:
        print('Fallo en la validación')


# -- Retorna una lista con una dupla del registro empleado [{}]
def getRecordEmpleado(run):
    startDto = EmpleadoDTO()
    data = startDto.findEmpleado(run)
    return data if data else False
 

def addEmpleado():
    try:
        run = valNoEmpty("Por favor ingrese su run: ") 
        name = valNoEmpty("Nombre: ") 
        lastName = valNoEmpty("Apellido: ") 
        #Muestra los cargos registrados
        findAllCargo()
        print("\nIngrese la descripción de un cargo registrado")
        cargo = valNoEmpty("Descripción del cargo: ").upper()
        address = valNoEmpty("Dirección: ").upper()
        password = valNoEmpty("Clave: ").upper()
        email = valNoEmpty("Correo electrónico: ").upper()
        #Muestra las comunas registrados
        findAllComuna()
        print("\nIngrese el nombre de una comuna registrada")
        comuna = valNoEmpty("Comuna: ").upper()

        if getRecordEmpleado(run):
            print(f'Ya hay un registro con el run {run} :(')
        else:
            # ----  Add to the database ----
            idcargo = getCargoRecordByName(cargo)[0]
            idcomuna = getComunaRecordByName(comuna)[0]
            
            startDto = EmpleadoDTO()  
            #run, nombre, apellido, cargo, direccion, clave, correo, comuna
            print(f'\n{startDto.addEmpleado(run=run, nombre=name, apellido=lastName, cargo=idcargo, direccion=address, clave=password, correo=email, comuna=idcomuna)}\n')
            

    except:
        print('Algo salió mal :(')   

def updateEmpleado():
    try:
        run = input("Por favor ingrese el run del empleado: ")
        if getRecordEmpleado(run):
            #actualiza
            print("\nIngrese un valor en los campos que quiera modificar\nSi no quiere modificar favor dejar en blanco")
            #Usuario ingresa los datos a actualizar
            runcambiado = input("\nPor favor ingrese nuevo rut: ")
            name = input("Nombre: ").upper()
            lastName = input("Apellido: ").upper()
            #Muestra los cargos registrados
            findAllCargo()
            print("\nIngrese la descripción de un cargo registrado")
            cargo = input("Descripción del cargo: ").upper()
            address = input("Dirección: ").upper()
            password = input("Clave: ")
            email = input("Corre electrónico: ").upper()
            #Muestra las comunas registrados
            findAllComuna()
            print("\nIngrese el nombre de una comuna registrada")
            comuna = input("Comuna: ").upper()

            idcargo = getCargoRecordByName(cargo)[0] if cargo else cargo
            idcomuna = getComunaRecordByName(comuna)[0] if comuna else comuna
            idBD = getRecordEmpleado(run)[0]

            print(f'\n{EmpleadoDTO().updateEmpleado(idBD=idBD, run=runcambiado, nombre=name, apellido=lastName, cargo=idcargo, direccion=address, clave=password, correo=email, comuna=idcomuna)}\n')

        else:
            print(f'No existe un registro con el run {run} :(')
    except:
        print('Algo salió mal :( update_empleado')


def delEmpleado():
    try: 
        run = input('Ingrese el run del empleado que desea eliminar: ')
        if getRecordEmpleado(run):
            ok = input(f'\n¿Está seguro que desea eliminar al empleado {getRecordEmpleado(run)[4]} {getRecordEmpleado(run)[5]}?: (si/no)')
            if ok:
                startDto = EmpleadoDTO()
                print('\n Eliminado exitosamente') if startDto.delEmpleado(run=run) else print('Algo salió mal :(')
        else:        
            print('No se encuentra ese registro\n') 

    except:
        print('Algo salió mal :(')

def findEmpleadoByComuna():
    try:
        #Muestra las comunas registrados
        findAllComuna()
        print("\nIngrese el nombre de una comuna registrada, \npara ver los empleados de esa comuna \n-----------------------------------\n")
        comuna = input("Comuna: ").upper()
        idcomunaDB = getComunaRecordByName(comuna)[0] if getComunaRecordByName(comuna) else False

        if idcomunaDB:
            startDto = EmpleadoDTO()
            EmpleadosDB = startDto.findEmpleadoByComuna(idcomunaDB)
            print(f"\nEmpleados de la comuna {comuna}\n ------------------------ ")
            for emp in EmpleadosDB:
                cargo = getRecordByID_Cargo(emp[1])[2]
                print(f'Run: {emp[3]} \nNombre: {emp[4]} {emp[5]} \nCargo: {cargo} \nComuna: {comuna} \nEmail: {emp[8]} \nDirección: {emp[6]}\n')
    except:
        print("Error findEmpleadoByComuna")

def findEmpleadoByCargo():
    try:
        #Muestra las comunas registrados
        findAllCargo()
        print("\nIngrese el nombre de un cargo registrado, \npara ver los empleados en esa función \n-----------------------------------\n")
        cargo = input("Cargo: ").upper()
        idcargoDB = getCargoRecordByName(cargo)[0] if getCargoRecordByName(cargo) else False

        if idcargoDB:
            startDto = EmpleadoDTO()
            EmpleadosDB = startDto.findEmpleadoByCargo(idcargoDB)
            print(f"\nEmpleados con el cargo {cargo}\n ------------------------ ")
            for emp in EmpleadosDB:
                comuna = getRecordByID_Comuna(emp[2])[2]
                print(f'Run: {emp[3]} \nNombre: {emp[4]} {emp[5]} \nCargo: {cargo} \nComuna: {comuna} \nEmail: {emp[8]} \nDirección: {emp[6]}\n')
    except:
        print("Error findEmpleadoByCargo")


def optionsEmpleado():
    print("Menu empleados\n -------------")
    print("""
        1. Ingresar Empleado
        2. Modificar Empleado
        3. Eliminar Empleado
        4. Mostrar Empleados por cargo
        5. Mostrar Empleados por comuna
        6. Salir de sistema
        """)
    op = int(input("Ingrese un número del menú: "))
    return op

