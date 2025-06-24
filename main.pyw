
from auth.login import mostrar_login
from database.db_manager import crear_tablas
crear_tablas()
import socket
import sys

def verificar_instancia_unica():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 65432))  # Puerto fijo
    except socket.error:
        print("Otra instancia ya está en ejecución.")
        sys.exit()
        
if __name__ == "__main__":
    verificar_instancia_unica()
    mostrar_login()