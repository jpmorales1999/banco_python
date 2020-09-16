import config.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Transaccion:

    def depositar(self, cuenta_id, tipo, valor):

        sql = "INSERT INTO transacciones VALUES (null, %s, %s, %s)"
        transaccion = (cuenta_id, tipo, valor)

        try:
            cursor.execute(sql, transaccion)
            database.commit() 

            result = [cursor.rowcount]

        except:
            result = [0]

        return result

    def retirar(self, cuenta_id, tipo, valor):

        sql = "INSERT INTO transacciones VALUES (null, %s, %s, %s)"
        transaccion = (cuenta_id, tipo, valor)

        try:
            cursor.execute(sql, transaccion)
            database.commit() 

            result = [cursor.rowcount]

        except:
            result = [0]

        return result

    def obtenerSaldo(self, id_cuenta):

        sql = "SELECT * FROM cuentas WHERE id = %s"

        cuenta = (id_cuenta)

        cursor.execute(sql, cuenta)
        result = cursor.fetchone()

        return result

    def consultarMovimientos(self, numero_cuenta):
        
        sql = "SELECT numero_cuenta, monto, tipo FROM cuentas JOIN transacciones ON cuentas.id=transacciones.cuenta_id JOIN tipos_transacciones ON transacciones.tipo_id=tipos_transacciones.id WHERE cuentas.numero_cuenta = %s"

        movimiento = (numero_cuenta)

        cursor.execute(sql, movimiento)
        result = cursor.fetchall()

        return result