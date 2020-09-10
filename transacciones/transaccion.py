import config.conexion as conexion

class Transaccion:

    def depositar(self, cuenta_id, tipo, valor):
        print(f"{cuenta_id} {tipo} {valor}")

        sql = "INSERT INTO transacciones VALUES (null, %s, %s, %s)"
        transaccion = (4, 3, 10000)

        try:
            cursor.execute(sql, transaccion)
            database.commit() 

            result = [cursor.rowcount]

        except:
            result = [0]

        return result