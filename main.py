# from controlador.validations import  validateName, inicial, validarLogin
from controlador.menus import startCargo
from controlador.menus import startComuna
from controlador.menus import mainMenu
from controlador.val_empleado import validarLogin

#### login
intentos = 1
login = False
print("\n---- Sistema Minimarket ----\n")
while intentos <= 3:
    try:
        resu = validarLogin()

        if resu is not None:
            login = True
            while login:
                print(f"\nBienvenido(a) Sr(a). : Administrador")
                op = mainMenu()
                if (op == 1):
                  print('\n... En construcción\n')

                elif (op == 2):
                  startCargo()
                
                elif (op == 3):
                  startComuna()

                else:
                  login = False
                  break;
                  
            
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamengte")
if intentos == 4:
    print("contraseña boqueada")



