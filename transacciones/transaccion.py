import config.conexion as conexion
import datetime
import helpers.helpers as encrypt

encriptar = encrypt.Helpers()

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Transaccion:

    def depositar(self, cuenta_id, tipo, valor):

        fecha = datetime.datetime.now()

        sql = "INSERT INTO transacciones VALUES (null, %s, null, %s, %s, %s)"
        transaccion = (cuenta_id, tipo, valor, fecha)

        try:
            cursor.execute(sql, transaccion)
            database.commit() 

            result = [cursor.rowcount]

        except:
            result = [0]

        return result

    def retirar(self, cuenta_id, tipo, valor):

        fecha = datetime.datetime.now()

        sql = "INSERT INTO transacciones VALUES (null, %s, null, %s, %s, %s)"
        transaccion = (cuenta_id, tipo, valor, fecha)

        try:
            cursor.execute(sql, transaccion)
            database.commit() 

            result = [cursor.rowcount]

        except:
            result = [0]

        return result

    def transferencia(self, cuenta_id, remitente, tipo, valor):
        fecha = datetime.datetime.now()

        sql = "INSERT INTO transacciones VALUES (null, %s, %s, %s, %s, %s)"
        transaccion = (cuenta_id, remitente, tipo, valor, fecha)

        try:
            cursor.execute(sql, transaccion)
            database.commit() 

            result = [cursor.rowcount]

        except:
            result = [0]

        return result

    def obtenerSaldo(self):

        sql = "SELECT id, saldo, numero_cuenta FROM cuentas"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def consultarMovimientos(self):
        
        sql = "SELECT nombre, apellidos, numero_cuenta, monto, fecha_hora, tipo, cuenta_remitente FROM cuentas JOIN transacciones ON cuentas.id=transacciones.cuenta_id JOIN tipos_transacciones ON transacciones.tipo_id=tipos_transacciones.id JOIN usuarios ON usuarios.cedula=cuentas.usuario_cedula ORDER BY transacciones.id DESC"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def actualizarSaldo(self, cuenta_id, saldo):

        sql = "UPDATE cuentas SET saldo = %s WHERE id = %s"

        cuenta = (saldo, cuenta_id)

        cursor.execute(sql, cuenta)

        database.commit()

