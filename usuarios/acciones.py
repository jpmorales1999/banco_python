import usuarios.usuario as modeloUsuario
import cuentas.acciones as accionesCuenta
import helpers.helpers as encrypt
from colorama import *

init()

# Instanciar clase Helpers
objeto = encrypt.Helpers()

class Acciones:

    def registro():
        errores = list()

        print(Fore.YELLOW + "\nGenial!! Vamos a registrarte en el sistema BancoCartago... ")

        print(Fore.CYAN)

        cedula = input('Introduce tu cédula: ').strip()
        nombre = input('Introduce tu nombre: ').upper().strip()
        apellidos = input('Introduce tus apellidos: ').upper().strip()
        email = input('Introduce tu email: ').strip()
        password = input('Introduce tu contraseña: ').lower().strip()

        if cedula.isnumeric() == False:
            errores.append("La cédula debe contener solo números")
        
        if nombre.isalpha() == False:
            errores.append("El nombre debe contener solo letras")
        
        if apellidos.isalpha() == False:
            errores.append("Los apellidos deben contener solo letras")

        if not "@" in email:
            errores.append("El correo electrónico es inválido")

        if len(password) < 6:
            errores.append("La contraseña debe ser mayor o igual a 6 carácteres")

        if len(errores) > 0:
            print("\n Se encontraron los siguientes errores: \n")
            for error in errores:
                print(Fore.RED + f"* {error}")
        else:
            # Cifrado Cédula
            cifradoCedula = objeto.encriptar_numero(cedula)

            # Cifrar Email
            cifradoEmail = objeto.encriptar_cadena(email)

            # Cifrar Password
            cifradoPassword = objeto.encriptar_cadena(password)

            usuario =  modeloUsuario.Usuario(cifradoCedula, nombre, apellidos, cifradoEmail, cifradoPassword)
            registro = usuario.registrar()

            if registro[0] >= 1:
                print(Fore.YELLOW + f'\nPerfecto {registro[1].nombre} te has registrado satisfactoriamente!!')

                cuenta = accionesCuenta.Acciones(registro[1].cedula)
                cuenta.crear_cuenta()

            else:
                print('\nNo te has registrado correctamente...!!')

    def login():

        print(Fore.YELLOW + "\nGenial!! Ingresa tus credenciales")

        print(Fore.CYAN)

        try:
            email = input('Introduce tu email: ')
            password = input('Introduce tu contraseña: ').lower()

            # Cifrar Correo
            cifradoEmail = objeto.encriptar_cadena(email)

            # Cifrar Contraseña
            cifradoPassword = objeto.encriptar_cadena(password)

            usuario = modeloUsuario.Usuario('', '', '', cifradoEmail, cifradoPassword)
            login = usuario.identificar()
            
            if cifradoEmail == login[3]:
                print(Fore.YELLOW + f'\nBienvenido {login[1]} {login[2]}, has ingresado en el sistema!!')

                cuenta = accionesCuenta.Acciones(login[0])
                cuenta.proximasAcciones(login)

        except Exception as e:

            print('\nLogin Incorrecto!!, Intentalo más tarde...\n')