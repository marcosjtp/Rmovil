import customtkinter as Ctk
DB_PATH = "repair_system.db"
APP_NAME = "Repair Manager"
COLOR_FONDO_VENTANA = "" 
FONDO_MENU=""# Color por defecto para la ventana principal
COLOR_TEXTO=""  # Color por defecto para el texto
MODO= ""  # Modo de apariencia por defecto

Ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
Ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

MODO =Ctk.get_appearance_mode()  # Te dará "Dark" o "Light"
if MODO == "Dark":
    FONDO_MENU = "#222831"  # Color más oscuro para menú
    COLOR_TEXTO = "white"  
    COLOR_FONDO_VENTANA = "#181a20"# Color más oscuro para la ventana principal
else:
    FONDO_MENU = "#f2f2f2"
    COLOR_TEXTO = "black"
    COLOR_FONDO_VENTANA =  "#f2f2f2"
    