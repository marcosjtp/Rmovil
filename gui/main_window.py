import customtkinter as Ctk
from gui.repair_form import abrir_formulario
from tkinter import ttk
from config import COLOR_FONDO_VENTANA, FONDO_MENU, COLOR_TEXTO, MODO
from database.db_manager import conectar
#variables globales
indice_actual = 0



        
def lanzar_ventana_principal():
    

    ventana = Ctk.CTk()
    ventana.title("Panel de Reparaciones")
    ventana.geometry("1024x600")
    ventana.minsize(800, 600)
    ventana.resizable(True, True)

    # Centrar ventana en pantalla
    ventana.update_idletasks()
     # Aplicar el tema antes de configurar la ventana
    ventana.config(bg=COLOR_FONDO_VENTANA)  # Usar el color de fondo definido en el tema
     # Configurar el tema de la aplicación
    ventana.wm_attributes("-topmost", 1)  # Mantener la ventana siempre
    width, height = 1024, 600
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")

    # Contenido
    Ctk.CTkLabel(
        ventana,
        text="Bienvenido al sistema de reparación",
        font=("Arial", 18, "bold")
    ).pack(pady=0)

    Ctk.CTkButton(
        ventana,
        text="Registrar nueva reparación",
        command=abrir_formulario
    ).pack(pady=10 , padx=10, fill="x")
    Frame1 = Ctk.CTkFrame(ventana, fg_color="black", corner_radius=10)
    Frame1.place(relx=0.5, rely=0.52, anchor="center", relwidth=0.98, relheight=0.8)
    #ubicacion de columnas de informacion
    treeScroll = ttk.Scrollbar(Frame1,orient="vertical")
    treeScroll.pack(side="right",fill="y")
         
    treeScrollx = ttk.Scrollbar(Frame1,orient="horizontal")
    treeScrollx.pack(side= "bottom",fill="x")  
    trv = ttk.Treeview(Frame1, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="15 ",yscrollcommand=treeScroll.set,xscrollcommand=treeScrollx.set)
    trv.pack()

    trv.heading(1, text="ID")
    trv.heading(2, text="Nombre")
    trv.heading(3, text="Apellido")
    trv.heading(4, text="Cedula")
    trv.heading(5, text="CiudadExpedicion")
    trv.heading(6, text="Direccion")
    trv.heading(7, text="Contrato")
    trv.heading(8, text="ARL")
    trv.heading(9, text="EPS")
    trv.heading(10, text="Fecha de nacimiento")
    treeScroll.config(command= trv.yview)
    treeScrollx.config(command=trv.xview,cursor="arrow")
    def CargarData(treeview):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reparaciones")
        registros = cursor.fetchall()
        conn.close()
    
        # Limpiar el Treeview antes de insertar nuevos datos
        for item in treeview.get_children():
            treeview.delete(item)

        # Insertar datos al Treeview
        for fila in registros:
            treeview.insert('', 'end', values=fila)
            
      # Llamar a la función para cargar datos en el Treeview
    # --- Botones de navegación (pequeños, en forma de triángulo) ---
    def obtener_registros():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reparaciones")
        datos = cursor.fetchall()
        conn.close()
        return datos

    def primer_registro(treeview):
        global indice_actual
        registros = obtener_registros()
        if registros:
            indice_actual = 0
            mostrar_registro(treeview, registros[indice_actual])

    def ultimo_registro(treeview):
        global indice_actual
        registros = obtener_registros()
        if registros:
            indice_actual = len(registros) - 1
            mostrar_registro(treeview, registros[indice_actual])

    def siguiente_registro(treeview):
        global indice_actual
        registros = obtener_registros()
        if registros and indice_actual < len(registros) - 1:
            indice_actual += 1
            mostrar_registro(treeview, registros[indice_actual])

    def registro_anterior(treeview):
        global indice_actual
        registros = obtener_registros()
        if registros and indice_actual > 0:
            indice_actual -= 1
            mostrar_registro(treeview, registros[indice_actual])

    def mostrar_registro(treeview, fila):
        # Limpiar el Treeview
        for item in treeview.get_children():
            treeview.delete(item)

    # Insertar el registro actual
        treeview.insert('', 'end', values=fila)
        
        
        
    nav_frame = Ctk.CTkFrame(ventana, fg_color="transparent", width=200, height=40)
    nav_frame.place(relx=0.5, rely=1.0, anchor="s", y=-6)  # centrado horizontal y pegado abajo

    btn_nav_primero = Ctk.CTkButton(nav_frame, text="⏮", width=40, height=32, fg_color="teal", font=("Arial", 16),command=lambda: primer_registro(trv))     
    btn_nav_primero.grid(row=0, column=0, padx=5)

    btn_nav_anterior = Ctk.CTkButton(nav_frame, text="◀", width=40, height=32, fg_color="teal", font=("Arial", 16),command=lambda: registro_anterior(trv))
    btn_nav_anterior.grid(row=0, column=1, padx=5)

    btn_nav_siguiente = Ctk.CTkButton(nav_frame, text="▶", width=40, height=32, fg_color="teal", font=("Arial", 16),command=lambda: siguiente_registro(trv))
    btn_nav_siguiente.grid(row=0, column=2, padx=5)

    btn_nav_ultimo = Ctk.CTkButton(nav_frame, text="⏭", width=40, height=32, fg_color="teal", font=("Arial", 16),command=lambda: ultimo_registro(trv))
    btn_nav_ultimo.grid(row=0, column=3, padx=5)
    
    CargarData(trv)
    ventana.mainloop()