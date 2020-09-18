import transacciones.transaccion as modeloTransaccion
import helpers.helpers as encrypt
from colorama import *

init()

objeto = modeloTransaccion.Transaccion()
encriptar = encrypt.Helpers()

class Acciones:

    def __init__(self, usuario):
        self.saldo = usuario[5]

    def consultar(self, usuario):
        email = encriptar.desencriptar_cadena(usuario[3])
        
        print(Fore.GREEN + "\n************************************************")
        print(f"Titular de la Cuenta: {usuario[1]} {usuario[2]}")
        print(f"Correo Electrónico del Titular: {email}")
        print(f"Número de la Cuenta: {usuario[4]}")
        print(f"Saldo total de la Cuenta: $ {usuario[5]}")
        print(f"Id de la Cuenta: $ {usuario[6]}")
        print("**************************************************")

    def proximasAcciones(self, remitente, usuario, tipo, valor):
        if tipo == 1:
            print(Fore.YELLOW + f"\nVamos a tranferir de tu cuenta $ {valor} pesos a la cuenta {remitente}")

            if self.saldo >= valor:
                
                transferencia = objeto.transferencia(usuario[6], remitente, tipo, valor)
                
                if transferencia[0] >= 1:
                    print(f'\nSe realizó la transferencia de manera Satisfactoria!!')
                    self.saldo = self.saldo - valor
                    objeto.actualizarSaldo(usuario[6], self.saldo)
                    cantidad_actual_saldo_remitente = objeto.obtenerSaldo()
                    for saldo in cantidad_actual_saldo_remitente:
                        if remitente == saldo[2]:
                            saldo_nuevo = saldo[1] + valor
                            objeto.actualizarSaldo(saldo[0], saldo_nuevo)
                    print(f"\nEl saldo actual en la cuenta es: {self.saldo}")
                else:
                    print('\nNo se logró realizar la transferencia correctamente...!!')

            else:
                print(f'\nNo cuentas con la cantidad digitada para Realizar la Transferencia!!')


        elif tipo == 2:
            print(Fore.YELLOW + f"\nVamos a retirar de tu cuenta $ {valor}")

            if self.saldo >= valor:
                retiro = objeto.retirar(usuario[6], tipo, valor)

                if retiro[0] >= 1:
                    print(f'\nSe realizó el retiro de manera Satisfactoria!!')
                    self.saldo = self.saldo - valor
                    objeto.actualizarSaldo(usuario[6], self.saldo)
                    print(f"El saldo actual en la cuenta es: {self.saldo}")
                else:
                    print('\nNo se logró realizar el retiro correctamente...!!')

            else:
                print(f'\nNo cuentas con la cantidad digitada para Realizar el Retiro!!')

        elif tipo == 3:
            print(Fore.YELLOW + f"\nVamos a depositar en tu cuenta $ {valor}")
            deposito = objeto.depositar(usuario[6], tipo, valor)

            if deposito[0] >= 1:
                print(f'\nSe realizó el deposito de manera Satisfactoria!!')
                self.saldo = self.saldo + valor
                objeto.actualizarSaldo(usuario[6], self.saldo)
                print(f"El saldo actual en la cuenta es: {self.saldo}")
            else:
                print('\nNo se logró realizar el deposito correctamente...!!')
                
    def depositar(self, usuario):
        deposito = int(input('Ingresa cantidad a Depositar: '))
        self.proximasAcciones(0, usuario, 3, deposito)

    def retirar(self, usuario):
        retiro = int(input('Ingresa cantidad a Retirar: '))
        self.proximasAcciones(0, usuario, 2, retiro)

    def transferencia(self, usuario):
        transferencia = int(input('Ingresa cantidad a Transferir: '))
        cuenta = int(input('Ingresa número de cuenta a Transferir: '))
        self.proximasAcciones(cuenta, usuario, 1, transferencia)

    def consultarSaldo(self, usuario):
        saldos = objeto.obtenerSaldo()
        for saldo in saldos:
            if saldo[0] == usuario[6]:
                print(Fore.YELLOW + f"\n{usuario[1]} {usuario[2]} Tú saldo actual es: {self.saldo}")

    def movimientos(self, usuario):
        print("\nTus últimos movimientos son los Siguientes...!!")
        movimientos = objeto.consultarMovimientos()
        for movimiento in movimientos:
            if movimiento[2] == usuario[4]:
                if movimiento[5] == "RETIRO":
                    print(Fore.RED + "\n***************************************")
                    print(f"Fecha y Hora: {movimiento[4]}")
                    print(f"Tipo de Acción Bancaria: {movimiento[5]}")
                    print(f"Nombre del Responsable: {movimiento[0]} {movimiento[1]}")
                    print(f"Número de Cuenta: {movimiento[2]}")
                    print(f"Monto de la Transferencia: {movimiento[3]}")
                    print("***************************************\n")
                elif movimiento[5] == "DEPOSITO":
                    print(Fore.GREEN + "\n***************************************")
                    print(f"Fecha y Hora: {movimiento[4]}")
                    print(f"Tipo de Acción Bancaria: {movimiento[5]}")
                    print(f"Nombre del Responsable: {movimiento[0]} {movimiento[1]}")
                    print(f"Número de Cuenta: {movimiento[2]}")
                    print(f"Monto de la Transferencia: {movimiento[3]}")
                    print("***************************************\n")
                elif movimiento[5] == "TRANSFERENCIA":
                    print(Fore.BLUE + "\n***************************************")
                    print(f"Fecha y Hora: {movimiento[4]}")
                    print(f"Tipo de Acción Bancaria: {movimiento[5]}")
                    print(f"Nombre del Responsable: {movimiento[0]} {movimiento[1]}")
                    print(f"Número de Cuenta: {movimiento[2]}")
                    print(f"Número de Cuenta Remitente: {movimiento[6]}")
                    print(f"Monto de la Transferencia: {movimiento[3]}")
                    print("***************************************\n")