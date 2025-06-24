import sqlite3
from config import DB_PATH

def conectar():
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            contrasena TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reparaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            dispositivo TEXT,
            telefono TEXT,
            email TEXT,            
            falla TEXT,
            nota TEXT,
            fecha_ingreso TEXT,
            estado TEXT,
            tecnico TEXT
            
            
        )
    """)
    conn.commit()
    conn.close()

def verificar_usuario(usuario, contrasena):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
    resultado = cursor.fetchone()
    conn.close()
    return bool(resultado)

def registrar_reparacion(cliente,telefono,email, dispositivo, falla, fecha_ingreso, estado,nota,tecnico):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reparaciones (cliente,telefono,email, dispositivo, falla, fecha_ingreso, estado,nota,tecnico)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (cliente,telefono,email, dispositivo, falla, fecha_ingreso, estado,nota,tecnico))
    conn.commit()
    conn.close()