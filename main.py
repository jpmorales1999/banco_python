"""
   Sistema Bancario - Mundo_Banco # Juan Pablo Morales Tames 
"""

from usuarios import acciones
from colorama import *

init()

print(Fore.YELLOW + "\n¡¡Bienvenido al Sistema Bancario BancoCartago!!")

print(Fore.CYAN + """
    Acciones Disponibles:
        1. Registrarse
        2. Ingresar
""")

objeto = acciones.Acciones

accion = int(input("¿Qué acción quieres realizar?: "))

if accion == 1:
    objeto.registro()
elif accion == 2:
    objeto.login()