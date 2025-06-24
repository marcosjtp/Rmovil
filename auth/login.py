import customtkinter as Ctk
from tkinter import messagebox
from database.db_manager import verificar_usuario
from gui.main_window import lanzar_ventana_principal

def mostrar_login():
    Ctk.set_appearance_mode("system")
    Ctk.set_default_color_theme("blue")

    ventana = Ctk.CTk()
    ventana.title("Login")
    ventana.geometry("400x300")
    ventana.resizable(False, False)

    # Centramos la ventana
    ventana.update_idletasks()
    width = 400
    height = 300
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")

    Ctk.CTkLabel(ventana, text="Iniciar Sesión", font=("Arial", 20, "bold")).pack(pady=20)
    user_entry = Ctk.CTkEntry(ventana, placeholder_text="Usuario")
    user_entry.pack(pady=10, padx=40, fill="x")
    pass_entry = Ctk.CTkEntry(ventana, placeholder_text="Contraseña", show="•")
    pass_entry.pack(pady=10, padx=40, fill="x")

    def login():
        if verificar_usuario(user_entry.get(), pass_entry.get()):
            lanzar_ventana_principal()
            ventana.withdraw()
            
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    Ctk.CTkButton(ventana, text="Ingresar", command=login).pack(pady=20)
    ventana.mainloop()