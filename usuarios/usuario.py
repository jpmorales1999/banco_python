import datetime
import config.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, cedula, nombre, apellidos, email, password):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        sql = "INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)"
        usuario = (self.cedula, self.nombre, self.apellidos, self.email, self.password, fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit() 

            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        return result

    def identificar(self):
        sql = "SELECT cedula, nombre, apellidos, email, numero_cuenta, saldo, id FROM usuarios JOIN cuentas ON usuarios.cedula=cuentas.usuario_cedula WHERE usuarios.email = %s AND usuarios.pass = %s"

        usuario = (self.email, self.password)

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result