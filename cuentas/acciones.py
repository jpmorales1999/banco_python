from random import randrange
import helpers.helpers as encrypt
import cuentas.cuenta as modeloCuenta
import transacciones.acciones as accionesTransacciones
from colorama import *

init()

# Instanciar clase Helpers
objeto = encrypt.Helpers()

class Acciones:

    def __init__(self, cedula):
        self.cedula = cedula
        self.cuenta = randrange(100000000)
        self.saldo = 0

    def crear_cuenta(self):

        cuenta = modeloCuenta.Cuenta(self.cedula, self.cuenta, self.saldo)
        registroCuenta = cuenta.crear()

        if registroCuenta[0] >= 1:
            print(f'\nSe ha registrado tu cuenta satisfactoriamente!!')
        else:
            print('\nNo se ha registrado tu cuenta correctamente...!!')

    def proximasAcciones(self, usuario):
            accion = 1

            objeto = accionesTransacciones.Acciones(usuario)

            while accion != 7:

                print(Fore.CYAN + """
                    Bienvenido a Mundo Banco!!! \n
                    Acciones Disponibles:
                        1. Consultar Cuenta
                        2. Depositar Saldo
                        3. Realizar Transferencia
                        4. Retirar Saldo
                        5. Consultar Saldo
                        6. Consultar Movimientos
                        7. Salir
                """) 

                accion = int(input("¿Qué quieres hacer?: "))
                
                if accion == 1:
                    objeto.consultar(usuario)
                elif accion == 2:
                    objeto.depositar(usuario)
                elif accion == 3:
                    objeto.transferencia(usuario)
                elif accion == 4:
                    objeto.retirar(usuario)
                elif accion == 5:
                    objeto.consultarSaldo(usuario)
                elif accion == 6:
                    objeto.movimientos(usuario)
                else:
                    print(Fore.YELLOW + f"\nAdiós {usuario[1]} {usuario[2]} vuelve Pronto!!!")
        