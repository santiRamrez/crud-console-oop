# from controlador.validations import  validateName, inicial, validarLogin
from controlador.menus import startCargo
from controlador.menus import startComuna
from controlador.menus import mainMenu
from controlador.menus import startEmpleado


# Login de acceso al programa
from controlador.val_empleado import validarLogin

#### login
intentos = 1
login = False
on = True
print("\n---- Sistema Minimarket ----\n")
while intentos <= 3 and on:
    try:
        resu = validarLogin()

        if resu is not None:
            login = True
            while login:
                print(f"Bienvenido(a) Sr(a). : Administrador")
                op = mainMenu()
                if (op == 1):
                  startEmpleado()

                elif (op == 2):
                  startCargo()
                
                elif (op == 3):
                  startComuna()

                else:
                  login = False
                  on = False
                  break;
                  
            
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamengte")
if intentos == 4:
    print("contraseña bloqueada")



