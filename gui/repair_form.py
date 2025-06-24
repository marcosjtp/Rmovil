import customtkinter as Ctk
from tkinter import messagebox
from database.db_manager import registrar_reparacion
from datetime import datetime

def abrir_formulario():
    Ctk.set_appearance_mode("system")  # Puede ser "light", "dark" o "system"
    Ctk.set_default_color_theme("dark-blue")  # Puedes cambiar a "green", "dark-blue", etc.

    ventana = Ctk.CTkToplevel()
    ventana.title("Registrar Reparación")
    ventana.geometry("400x600")
    ventana.resizable(False, True)
    ventana.wm_attributes("-topmost", 1)

    # Centrar ventana
    ventana.update_idletasks()
    width, height = 400, 600
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")

    Ctk.CTkLabel(ventana, text="Formulario de Reparación", font=("Arial", 18, "bold")).pack(pady=20)

    entradas = {}

    for campo in ["Cliente","telefono","email", "Dispositivo", "Falla","nota","tecnico", "estado"]:
        label = Ctk.CTkLabel(ventana, text=campo)
        label.pack(padx=40, anchor="w")
        entrada = Ctk.CTkEntry(ventana,fg_color="teal",placeholder_text=f"Ingrese {campo.lower()}")
        entrada.pack(padx=40, pady=(0, 15), fill="x")
        entradas[campo] = entrada

    def guardar():
        cliente = entradas["Cliente"].get()
        dispositivo = entradas["Dispositivo"].get()
        telefono = entradas["telefono"].get()
        email = entradas["email"].get()        
        falla = entradas["Falla"].get()
        nota = entradas["nota"].get()
        tecnico = entradas["tecnico"].get()
        estado = entradas["estado"].get()
        

        if not cliente or not dispositivo or not falla:
            messagebox.showwarning("Faltan datos", "Por favor completa todos los campos.", parent=ventana)
            return

        fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M")
        registrar_reparacion(cliente,telefono,email, dispositivo, falla, fecha_ingreso, estado,nota,tecnico)
        messagebox.showinfo("Guardado", "Reparación registrada con éxito.")
        ventana.destroy()

    Ctk.CTkButton(ventana, text="Guardar Reparación", command=guardar).pack(pady=20)