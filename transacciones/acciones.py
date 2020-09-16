import transacciones.transaccion as modeloTransaccion

objeto = modeloTransaccion.Transaccion()

class Acciones:

    def __init__(self, usuario):
        self.saldo = usuario[5]

    def consultar(self, usuario):
        print("\n****************************************")
        print(f"Titular de la Cuenta: {usuario[1]} {usuario[2]}")
        print(f"Correo Electrónico del Titular: {usuario[3]}")
        print(f"Número de la Cuenta: {usuario[4]}")
        print(f"Saldo total de la Cuenta: $ {usuario[5]}")
        print(f"Id de la Cuenta: $ {usuario[6]}")
        print("******************************************")

    def proximasAcciones(self, usuario, tipo, valor):
        if tipo == 2:
            print(f"\nVamos a retirar de tu cuenta $ {valor}")
            retiro = objeto.retirar(usuario[6], tipo, valor)

            if retiro[0] >= 1:
                print(f'\nSe realizó el retiro de manera Satisfactoria!!')
            else:
                print('\nNo se logró realizar el retiro correctamente...!!')

        elif tipo == 3:
            print(f"\nVamos a depositar en tu cuenta $ {valor}")
            deposito = objeto.depositar(usuario[6], tipo, valor)

            if deposito[0] >= 1:
                print(f'\nSe realizó el deposito de manera Satisfactoria!!')
            else:
                print('\nNo se logró realizar el deposito correctamente...!!')
                
    def depositar(self, usuario):
        deposito = int(input('Ingresa cantidad a Depositar: '))
        self.proximasAcciones(usuario, 3, deposito)

    def retirar(self, usuario):
        retiro = int(input('Ingresa cantidad a Retirar: '))
        self.proximasAcciones(usuario, 2, retiro)

    def movimientos(self, usuario):
        print("\nTus últimos movimientos son los Siguientes...!!")
        objeto.consultarMovimientos(usuario[4])