# ---- Paquetes de este sistema ----
from controlador.dto_comuna import ComunaDTO
from modelo.comuna import Comuna

def getComunaRecordByName(name):
    if name:
        data = ComunaDTO().getRecordByName(name)
        return data
    else:
        return ""

def getRecordByID_Comuna(id):
    if id:
        data = ComunaDTO().getRecordByID(id)
        return data
    else:
        return ""

def findComuna(a):
    identi = int(a)
    if identi > 0:
      data = ComunaDTO().startDto.findComuna(identi)
      return data

def addComuna():
    try:
        name = input('Ingrese la descripción de la comuna: ')
        num = int(input('Ingrese el id de la comuna: '))
        if len(name) > 1 and num > 0:
            if findComuna(num):
                print('La comuna ya existe :( , vuelva a intenar con otro id\n')
                addComuna()
            else:
                # ----  Add to the local memory ----
                initComuna = Comuna(descripcionComuna=name.upper(), idComuna=num)
                Comuna().getListaComuna().append(initComuna)
                # ----  Add to the database ----
                startDto = ComunaDTO()
                print(f'\n{startDto.addComuna(description=name.upper(), id=num)}\n')
        else:
            print('\nError en el ingreso :(, vuelva a intentar\n')
            addComuna()
    except:
        print('Algo salió mal :( ')


def updateComuna():
    try: 
        id = input('Ingrese el id de la comuna que desea modificar: ')
        if findComuna(id):
            name = input('Ingrese el nuevo nombre del cargo: ')
            if len(name) > 0:
                startDto = ComunaDTO()
                print(f'\n{startDto.updateComuna(id=id, description=name.upper())}')
        else:        
            print('No se encuentra ese registro\n') 

    except:
        print('Algo salió mal :(')


def delComuna():
    try: 
        id = input('Ingrese el id del cargo que desea eliminar: ')
        if findComuna(id):
            startDto = ComunaDTO()
            print('\n Eliminado exitosamente') if startDto.delComuna(id=id) else print('Algo salió mal :(')
        else:        
            print('No se encuentra ese registro\n') 

    except:
        print('Algo salió mal :(')


def findAllComuna():
    startDto = ComunaDTO()
    list = startDto.findAllComuna()
    if len(list) > 0:
        print('\n    Id   |   Comuna ')
        for record in list:
          print(' ----------------------------- ')
          print(f'    {record[1]}   |   {record[2]}   ')
    else:
        print('\nNo hay registros que mostrar :(')  



def optionsComuna():
    print('\nEstás en el menú COMUNAS: \n------------------------')
    print(''' 
      1. Ingresar comuna.
      2. Modificar comuna.
      3. Eliminar comuna.
      4. Mostrar todas las comunas.
      5. Volver al menu principal.
    ''')



