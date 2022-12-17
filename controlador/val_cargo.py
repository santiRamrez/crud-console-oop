# ---- Paquetes de este sistema ----
from controlador.dto_cargo import CargoDTO
from modelo.cargo import Cargo

# ---- Retorna el registro de cargo en forma de dupla
def getCargoRecordByName(name):
    if name:
        data = CargoDTO().getRecordByName(name)
        return data
    else:
        return ""


def findCargo(a):
    identi = int(a)
    if identi > 0:
      startDto = CargoDTO()
      return startDto.findCargo(identi)

def addCargo():
    try:
        name = input('Ingrese la descripción del cargo: ')
        num = int(input('Ingrese el id del cargo: '))
        if len(name) > 1 and num > 0:
            if findCargo(num):
                print('El cargo ya existe :( , vuelva a intenar con otro id\n')
                addCargo()
            else:
                # ----  Add to the local memory ----
                initCargo = Cargo(descripcionCargo=name.upper(), idCargo=num)
                Cargo().getListaCargo().append(initCargo)
                # ----  Add to the database ----
                startDto = CargoDTO()
                print(f'\n{startDto.addCargo(description=name.upper(), id=num)}\n')
        else:
            print('\nError en el ingreso :(, vuelva a intentar\n')
            addCargo()
    except:
        print('Algo salió mal :(')


def updateCargo():
    try: 
        id = input('Ingrese el id del cargo que desea modificar: ')
        if findCargo(id):
            name = input('Ingrese el nuevo nombre del cargo: ')
            if len(name) > 0:
                startDto = CargoDTO()
                print(f'\n{startDto.updateCargo(id=id, description=name.upper())}')
        else:        
            print('No se encuentra ese registro\n') 

    except:
        print('Algo salió mal :(')


def delCargo():
    try: 
        id = input('Ingrese el id del cargo que desea eliminar: ')
        if findCargo(id):
            startDto = CargoDTO()
            print('\n Eliminado exitosamente') if startDto.delCargo(id=id) else print('Algo salió mal :(')
        else:        
            print('No se encuentra ese registro\n') 

    except:
        print('Algo salió mal :(')


def findAllCargo():
    startDto = CargoDTO()
    list = startDto.findAllCargo()
    if len(list) > 0:
        print('\n    Id  | Descripcion ')
        for record in list:
          print(' ----------------------------- ')
          print(f'    {record[1]}   |   {record[2]}   ')
    else:
        print('\nNo hay registros que mostrar :(')  



def optionsCargo():
    print('\nEstás en el menú CARGOS: \n------------------------')
    print(''' 
      1. Ingresar cargo.
      2. Modificar cargo.
      3. Eliminar cargo.
      4. Mostrar todos los cargos.
      5. Volver al menu principal.
    ''')







    

