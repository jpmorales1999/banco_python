import usuarios.usuario as modeloUsuario
import cuentas.acciones as accionesCuenta
import helpers.helpers as encrypt

# Instanciar clase Helpers
objeto = encrypt.Helpers()

class Acciones:

    def registro():

        print("\nGenial!! Vamos a registrarte en el sistema BancoCartago... \n")

        cedula = input('Introduce tu cédula: ')
        nombre = input('Introduce tu nombre: ').upper()
        apellidos = input('Introduce tus apellidos: ').upper()
        email = input('Introduce tu email: ')
        password = input('Introduce tu contraseña: ').lower()

        # Cifrado Cédula
        cifradoCedula = objeto.encriptar_numero(cedula)

        # Cifrar Email
        cifradoEmail = objeto.encriptar_cadena(email)

        # Cifrar Password
        cifradoPassword = objeto.encriptar_cadena(password)

        usuario =  modeloUsuario.Usuario(cifradoCedula, nombre, apellidos, cifradoEmail, cifradoPassword)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f'\nPerfecto {registro[1].nombre} te has registrado satisfactoriamente!!')

            cuenta = accionesCuenta.Acciones(registro[1].cedula)
            cuenta.crear_cuenta()

        else:
            print('\nNo te has registrado correctamente...!!')

    def login():

        print("\nGenial!! Ingresa tus credenciales\n")

        try:
            email = input('Introduce tu email: ')
            password = input('Introduce tu contraseña: ')

            # Cifrar Correo
            cifradoEmail = objeto.encriptar_cadena(email)

            # Cifrar Contraseña
            cifradoPassword = objeto.encriptar_cadena(password)

            usuario = modeloUsuario.Usuario('', '', '', cifradoEmail, cifradoPassword)
            login = usuario.identificar()
            
            if cifradoEmail == login[3]:
                print(f'\nBienvenido {login[1]} {login[2]}, has ingresado en el sistema!!')

                cuenta = accionesCuenta.Acciones(login[0])
                cuenta.proximasAcciones(login)

        except Exception as e:

            print('\nLogin Incorrecto!!, Intentalo más tarde...\n')