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

    def proximasAcciones(self, cuenta_id, tipo, valor):
        if tipo == 3:
            print(f"\nVamos a depositar en tu cuenta $ {valor}")
            deposito = objeto.depositar(cuenta_id, tipo, valor)
            if deposito[0] >= 1:
                print("\nSe realizó el Deposito Correctamente!!!")
            else:
                print("\nNo se logró realizar el Deposito!!!")
                
    def depositar(self, usuario):
        deposito = int(input('Ingresa cantidad a Depositar: '))
        self.proximasAcciones(usuario[6], 3, deposito)