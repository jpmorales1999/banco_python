import mysql.connector

def conectar():
    
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="banco_cartago",
        port=3306
    )

    cursor = database.cursor()

    return [database, cursor]