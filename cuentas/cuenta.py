import config.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cuenta:

    def __init__(self, cedula, cuenta, saldo):
        self.cedula = cedula
        self.cuenta = cuenta
        self.saldo = saldo

    def crear(self):

        sql = "INSERT INTO cuentas VALUES (null, %s, %s, %s)"
        cuenta = (self.cedula, self.cuenta, self.saldo)

        try:
            cursor.execute(sql, cuenta)
            database.commit() 

            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        return result