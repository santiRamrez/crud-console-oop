# from controlador.dto_user import UserDTO

# ---- Cargo Controladores ----
from controlador.val_cargo import optionsCargo
from controlador.val_cargo import addCargo
from controlador.val_cargo import updateCargo
from controlador.val_cargo import delCargo
from controlador.val_cargo import findAllCargo

# ---- Comuna Controladores ----
from controlador.val_comuna import optionsComuna
from controlador.val_comuna import addComuna
from controlador.val_comuna import updateComuna
from controlador.val_comuna import delComuna
from controlador.val_comuna import findAllComuna

# ---- Empleado Controladores ----




def startCargo():
  while True:
    try:
      optionsCargo()
      op = int(input('Ingrese un número del menu para acceder a las opciones: '))
      
      if op == 5:
          break;
      
      elif op == 1:
          addCargo()

      elif op == 2:
          updateCargo()

      elif op == 3:
          delCargo()

      elif op == 4:
          findAllCargo()

    except:
        break;


def startComuna():
  while True:
    try:
      optionsComuna()
      op = int(input('Ingrese un número del menu para acceder a las opciones: '))
      
      if op == 5:
          break;
      
      elif op == 1:
          addComuna()

      elif op == 2:
          updateComuna()

      elif op == 3:
          delComuna()

      elif op == 4:
          findAllComuna()

    except:
        break;


def mainMenu():
    print(''' 
      1. CRUD Empleados.
      2. CRUD Cargos.
      3. CRUD Comunas.
      4. Cerrar programa.
    ''')
    try:
        op = int(input('Para acceder ingrese el número:  '))
        return op
    except:
        print('Favor ingrese una opcion valida')
    


