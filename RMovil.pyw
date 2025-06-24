from tkinter import ttk
import customtkinter as Ctk
import tkinter as tk
from tkinter import YES
from tkinter import messagebox,filedialog,StringVar,LabelFrame
import sqlite3
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from fpdf.fpdf import FPDF
import subprocess
from datetime import datetime
import sys
import socket
import PIL
from PIL import Image

Ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
Ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
current_date1 = datetime.now().strftime("%d")
current_date2 = datetime.now().strftime("%m")
current_date3 = datetime.now().strftime("%Y")
COLOR_FONDO = "#123452"
COLOR_ACTIVO = "orange"
COLOR_TEXTO = "yellow"
cursores=["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]


class Contratista: 
        
    def __init__(self, root):
        self.wind =root 
        self.wind.title ("Rmovil")
        self.wind.geometry("1090x600")
        self.wind.attributes('-fullscreen') 
        Frame1=Ctk.CTkFrame(self.wind ,bg_color="teal")
        Frame2=LabelFrame(self.wind)
#dimension Bordes
        Frame1.pack(fill="both", expand="yes", padx=20, pady=15 )
        Frame2.pack(fill="both", expand="yes", padx=20, pady=15 )

        self.Codigo=StringVar()
        self.Nombre=StringVar()
        self.telefono=StringVar()
        self.Descripcion=StringVar()
        self.Marca=StringVar()
        self.Modelo=StringVar()
        self.Serial=StringVar()
        self.Trab_a_real=StringVar()
        self.Fecha_ing=StringVar()
        self.trab_real=StringVar()
        self.Fecha_ent=StringVar()
        self.Falla=StringVar()
        self.Detalles=StringVar()
        self.Estado=StringVar()
        self.Conclusion=StringVar()
        self.Estadofinal=StringVar()
        
        
        

        modo =Ctk.get_appearance_mode()  # Te dará "Dark" o "Light"
        if modo == "Dark":
            fondo_menu = "#222831"  # Color más oscuro para menú
            color_texto = "white"
            color_fondo_ventana = "#181a20"  # Color más oscuro para la ventana principal
        else:
            fondo_menu = "#f2f2f2"
            color_texto = "black"
            color_fondo_ventana = "#f2f2f2"
        self.wind.config(bg=color_fondo_ventana)       
        def Primerasconeciones():
            print("Conectando...")

            try:
                miconeccion = sqlite3.connect("Data")
                micursor = miconeccion.cursor()
                messagebox.showinfo("Conexión", "La conexión con la base de datos fue exitosa.")

                # Crear la tabla si no existe
                micursor.execute("""
                    CREATE TABLE IF NOT EXISTS tblmovil (
                        codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        Nombre TEXT,
                        telefono TEXT,
                        Descripcion TEXT,
                        Marca TEXT,
                        Modelo TEXT,
                        Serial TEXT,
                        Trab_a_real TEXT,
                        Fecha_ing TEXT,
                        trab_real TEXT,
                        Fecha_ent TEXT,
                        Falla TEXT,
                        Detalles TEXT,
                        Estado TEXT,
                        Conclusion TEXT,
                        Estadofinal TEXT
                    )
                """)
                miconeccion.commit()
                messagebox.showinfo("Tabla", "La tabla 'tblmovil' se ha verificado o creado correctamente.")

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

            finally:
                try:
                    miconeccion.close()
                except:
                    pass
        def SalirApp(): self.wind.destroy()
        def Func_Guardar():
            print("Guardando...")

            try:
                miconeccion = sqlite3.connect("Data")
                micursor = miconeccion.cursor()

                # Extraemos los valores de los StringVar()
                datos = (
                    self.Nombre.get(),
                    self.telefono.get(),
                    self.Descripcion.get(),
                    self.Marca.get(),
                    self.Modelo.get(),
                    self.Serial.get(),
                    self.Trab_a_real.get(),
                    self.Fecha_ing.get(),
                    self.trab_real.get(),
                    self.Fecha_ent.get(),
                    self.Falla.get(),
                    self.Detalles.get(),
                    self.Estado.get(),
                    self.Conclusion.get(),
                    self.Estadofinal.get()
                )

                # Ejecutamos la consulta con placeholders
                micursor.execute("""
                    INSERT INTO Tblmovil VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, datos)

                miconeccion.commit()                
                messagebox.showinfo("Guardar", "Registro guardado con éxito")
                CargarData()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un problema al guardar:\n{e}")
            finally:
                miconeccion.close()
                  
        def Func_Actualizar():
            print("Actualizando...")

            try:
                miconeccion = sqlite3.connect("Data")
                micursor = miconeccion.cursor()

                # Recolectamos todos los datos desde las variables
                datos = (
                    self.Nombre.get(),
                    self.telefono.get(),
                    self.Descripcion.get(),
                    self.Marca.get(),
                    self.Modelo.get(),
                    self.Serial.get(),
                    self.Trab_a_real.get(),
                    self.Fecha_ing.get(),
                    self.trab_real.get(),
                    self.Fecha_ent.get(),
                    self.Falla.get(),
                    self.Detalles.get(),
                    self.Estado.get(),
                    self.Conclusion.get(),
                    self.Estadofinal.get(),
                    self.Codigo.get()  # Este va al final para el WHERE
                )

                micursor.execute("""
                    UPDATE Tblmovil SET
                        Nombre = ?,
                        telefono = ?,
                        Descripcion = ?,
                        Marca = ?,
                        Modelo = ?,
                        Serial = ?,
                        Trab_a_real = ?,
                        Fecha_ing = ?,
                        trab_real = ?,
                        Fecha_ent = ?,
                        Falla = ?,
                        Detalles = ?,
                        Estado = ?,
                        Conclusion = ?,
                        Estadofinal = ?
                    WHERE Codigo = ?
                """, datos)

                miconeccion.commit()
                messagebox.showinfo("Actualizar", "Registro actualizado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un problema al actualizar:\n{e}")
            finally:
                miconeccion.close()
                CargarData()
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        def funNuevo(): 
            print("Nuevo registro")
            try:
                    self.Codigo.set("")
                    self.Nombre.set("")
                    self.telefono.set("")
                    self.Descripcion.set("")
                    self.Marca.set("")
                    self.Modelo.set("")
                    self.Serial.set("")
                    self.Trab_a_real.set("")
                    self.Fecha_ing.set("")
                    self.trab_real.set("")
                    self.Fecha_ent.set("")
                    self.Falla.set("")
                    self.Detalles.set("")
                    self.Estado.set("")
                    self.Conclusion.set("")
                    self.Estadofinal.set("")
                    #self.Nombre.focus() # Suponiendo que tienes un Entry con nombre self.Codigo_Entry

            except:
                messagebox.showinfo("Error","No se ha encontrado que Limpiar")

        def Func_Delete(): 
            # Confirmar antes de eliminar
            if not self.Codigo.get():
                messagebox.showwarning("Advertencia", "Debe ingresar un código para eliminar.")
                return

            confirmar = messagebox.askyesno("Confirmar eliminación", "¿Realmente desea eliminar este registro?")
            if not confirmar:
                return

            print("Eliminando...")
            try:
                miconeccion = sqlite3.connect("Data")
                micursor = miconeccion.cursor()
                micursor.execute("DELETE FROM Tblmovil WHERE codigo=?", (self.Codigo.get(),))
                miconeccion.commit()
                messagebox.showinfo("Eliminar", "Registro eliminado con éxito")
                CargarData()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un problema al eliminar:\n{e}")
            finally:
                miconeccion.close()
        def FunPrimerRegistro(): print("Primer registro")
        def funSiguiente():
    # Obtener todos los IDs ordenados del Treeview
            items = self.trv.get_children()
            if not items:
                messagebox.showinfo("Información", "No hay registros en la tabla.")
                return

            # Buscar el seleccionado actual
            seleccionado = self.trv.focus()
            if not seleccionado:
                # Si nada está seleccionado, selecciona el primero
                self.trv.selection_set(items[0])
                self.trv.focus(items[0])
                self.trv.see(items[0])
                traineeInfo(None)
                return

            idx = items.index(seleccionado)
            if idx < len(items) - 1:
                siguiente = items[idx + 1]
                self.trv.selection_set(siguiente)
                self.trv.focus(siguiente)
                self.trv.see(siguiente)
                traineeInfo(None)
            else:
                messagebox.showinfo("Información", "Ya estás en el último registro.")
        def funAnterior():
            print("Anterior registro")
            # Obtener todos los IDs ordenados del Treeview
            items = self.trv.get_children()
            if not items:
                messagebox.showinfo("Información", "No hay registros en la tabla.")
                return

            # Buscar el seleccionado actual
            seleccionado = self.trv.focus()
            if not seleccionado:
                # Si nada está seleccionado, selecciona el último
                self.trv.selection_set(items[-1])
                self.trv.focus(items[-1])
                self.trv.see(items[-1])
                traineeInfo(None)
                return

            idx = items.index(seleccionado)
            if idx > 0:
                anterior = items[idx - 1]
                self.trv.selection_set(anterior)
                self.trv.focus(anterior)
                self.trv.see(anterior)
                traineeInfo(None)
            else:
                messagebox.showinfo("Información", "Ya estás en el primer registro.")
        def FunUltimoRegistro(): print("Último registro")
        def busquedaxemail(): print("Buscar por email")
        def busquedaxcodigo():
            print("Buscar por código")
            if not self.Codigo.get():
                messagebox.showwarning("Advertencia", "Debe ingresar un código para buscar.")
                return

            try:
                miconeccion = sqlite3.connect("Data")
                micursor = miconeccion.cursor()
                micursor.execute("SELECT * FROM tblmovil WHERE codigo=?", (self.Codigo.get(),))
                Dmovil = micursor.fetchall()
                miconeccion.commit()
                miconeccion.close()

                if not Dmovil:
                    messagebox.showinfo("Sin resultados", "Este código no existe. Ingrese un código correcto.")
                    self.Codigo.set("")
                    self.Codigo.focus()  # Suponiendo que tienes un Entry con nombre self.Codigo_Entry
                    return

                for Row in Dmovil:
                    self.Codigo.set(Row[0])
                    self.Nombre.set(Row[1])
                    self.telefono.set(Row[2])
                    self.Descripcion.set(Row[3])
                    self.Marca.set(Row[4])
                    self.Modelo.set(Row[5])
                    self.Serial.set(Row[6])
                    self.Trab_a_real.set(Row[7])
                    self.Fecha_ing.set(Row[8])
                    self.trab_real.set(Row[9])
                    self.Fecha_ent.set(Row[10])
                    self.Falla.set(Row[11])
                    self.Detalles.set(Row[12])
                    self.Estado.set(Row[13])
                    self.Conclusion.set(Row[14])
                    self.Estadofinal.set(Row[15])

                try:
                    self.trv.selection_set(self.Codigo.get())
                    self.trv.see(self.Codigo.get())
                except Exception:
                    pass

            except Exception as e:
                messagebox.showinfo("Error Lectura", f"No se ha podido leer el registro:\n{e}")

        def busquedaxcedula(): print("Buscar por cédula")
        def busquedaxtelefono(): print("Buscar por teléfono")
        def msjinfo(): print("Mostrando información...")
        
        def agregar_encabezado(pdf):
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, "MJ TECHNOLOGY", ln=True, align="C")

        def agregar_pie_pagina(pdf):
            pdf.set_y(-10)
            pdf.set_font("Arial", "I", 10)
            pdf.cell(0, 0, "  Gracias por Preferirnos", ln=True, align="C")

        def crearticket():
            crear = messagebox.askquestion("Crear Ticket", "Realmente Deseas Crear un Ticket")
            if crear != "yes":
                return

            class TicketPDF(FPDF):
                pass  # Sin header/footer automáticos

            # Estimación del alto del ticket
            lineas_fijas = 12
            lineas_terminos = 25
            alto_por_linea = 4
            alto_total = (lineas_fijas + lineas_terminos) * alto_por_linea + 20

            pdf = TicketPDF("P", "mm", (80, alto_total))
            pdf.add_page()

            # Encabezado
            agregar_encabezado(pdf)

            # Contenido
            pdf.set_font("Arial", "", 10)
            fecha_hora_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            pdf.cell(0, 5, f"Fecha: {fecha_hora_actual}", ln=True)
            pdf.cell(0, 5, f"Ticket No. : {self.Codigo.get()}", ln=True)
            pdf.cell(0, 5, f"Cliente: {self.Nombre.get()}", ln=True)
            pdf.cell(0, 5, "-" * 50, ln=True)
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 5, "Datos del equipo", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.cell(0, 4, f"{self.Descripcion.get()}  {self.Marca.get()} {self.Modelo.get()} {self.Serial.get()}", ln=True)

            pdf.cell(0, 5, "-" * 50, ln=True)
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 5, "Estado Previo del equipo", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 4, self.Trab_a_real.get(), align='J')
            pdf.cell(0, 5, "-" * 50, ln=True)
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 5, "Trabajo a Realizar", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 4, self.Trab_a_real.get(), align='J')
            pdf.cell(0, 5, "-" * 50, ln=True)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 5, "Términos y condiciones:", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 4,
                "\nAgradecemos su confianza y hacemos de su conocimiento las siguientes condiciones de servicio:\n"
                "- Después de 30 días los equipos pueden ser usados como remate o refacción...\n"
                "- Retire chip y memoria no nos hacemos responsables.\n"
                "- En equipos mojados, software, daños por mal uso e intervenidos no hay garantía.\n"
                "- La entrega del equipo será solo con nota o identificación.\n"
                "- Pueden existir variaciones entre la pieza original y el reemplazo...\n"
                "- El tiempo de entrega puede retrasarse si la refacción viene de proveedores externos.\n",
                align='J'
            )

            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 7, "Cualquier duda contáctenos:", ln=True)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 4, "(809-713-0087)", ln=True, align="C")

            # Pie de página
            #pdf.set_y(-10)
            pdf.set_font("Arial", "I", 10)
            pdf.cell(0, 4, "  Gracias por Preferirnos", ln=True, align="C")
            #agregar_pie_pagina(pdf)

            # Guardar y abrir el PDF
            nombre_archivo = f"ticket_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            pdf.output(nombre_archivo)
            subprocess.Popen(nombre_archivo, shell=True)
            print("¡Ticket generado exitosamente!")
        def flimpiar():
            try:
                # Limpiar el Treeview antes de volver a cargar
                for item in self.trv.get_children():
                    self.trv.delete(item)
            except Exception as e:
                messagebox.showinfo("Error Lectura", f"No se ha podido leer el registro:\n{e}")
             
        def CargarData():
            try:
                # Limpiar el Treeview antes de volver a cargar
                for item in self.trv.get_children():
                    self.trv.delete(item)

                miconeccion = sqlite3.connect("Data")
                micursor = miconeccion.cursor()
                micursor.execute("SELECT * FROM tblmovil WHERE codigo >= 1")
                EstudLeido = micursor.fetchall()
                miconeccion.commit()
                miconeccion.close()

                for estudiant in EstudLeido:
                    self.Codigo.set(estudiant[0])
                    self.Nombre.set(estudiant[1])
                    self.telefono.set(estudiant[2])
                    self.Descripcion.set(estudiant[3])
                    self.Marca.set(estudiant[4])
                    self.Modelo.set(estudiant[5])
                    self.Serial.set(estudiant[6])
                    self.Trab_a_real.set(estudiant[7])
                    self.Fecha_ing.set(estudiant[8])
                    self.trab_real.set(estudiant[9])
                    self.Fecha_ent.set(estudiant[10])
                    self.Falla.set(estudiant[11])
                    self.Detalles.set(estudiant[12])
                    self.Estado.set(estudiant[13])
                    self.Conclusion.set(estudiant[14])
                    self.Estadofinal.set(estudiant[15])

                    self.trv.insert(
                        parent="",
                        index="end",
                        iid=self.Codigo.get(),
                        values=(
                            self.Codigo.get(), self.Nombre.get(), self.telefono.get(), self.Descripcion.get(),
                            self.Marca.get(), self.Modelo.get(), self.Serial.get(), self.Trab_a_real.get(),
                            self.Fecha_ing.get(), self.trab_real.get(), self.Fecha_ent.get(), self.Falla.get(),
                            self.Detalles.get(), self.Estado.get(), self.Conclusion.get(),
                            self.Estadofinal.get()
                        )
                    )
            except Exception as e:
                messagebox.showinfo("Error Lectura", f"No se ha podido leer el registro:\n{e}")
        def traineeInfo(ev):
                viewInfo = self.trv.focus()
                learnerData = self.trv.item(viewInfo)
                row = learnerData['values']
                print("Elementos en row:", len(row))
                print("Contenido de row:", row)
                self.Codigo.set(row[0])
                self.Nombre.set(row[1])
                self.telefono.set(row[2])
                self.Descripcion.set(row[3])
                self.Marca.set(row[4])
                self.Modelo.set(row[5])
                self.Serial.set(row[6])
                self.Trab_a_real.set(row[7])
                self.Fecha_ing.set(row[8])
                self.trab_real.set(row[9])
                self.Fecha_ent.set(row[10])
                self.Falla.set(row[11])
                self.Detalles.set(row[12])
                self.Estado.set(row[13])
                self.Conclusion.set(row[14])
                self.Estadofinal.set(row[15])
        # Colores personalizados
        COLOR_BG = "#123452"
        COLOR_TEXTO = "yellow"
        COLOR_ACTIVO = "orange"
        COLOR_FG_ACTIVO = "red"
#:::::::::::::::::::::::::::::::::::::::::omienso Menu desplegable:::::::::::::::::::::::::::::::::::::::::::::: 
        # Crear la barra de menú
        barraMenu = tk.Menu(
            self.wind,
            background=fondo_menu,
            fg=color_texto,
            activebackground="#393e46",
            activeforeground="orange",
            bd=0,
            relief="flat"
        )
        self.wind.config(menu=barraMenu)

        # Función auxiliar para crear menús
        def crear_menu(nombre, items):
            menu = tk.Menu(
                barraMenu,
                tearoff=0,
                bg=fondo_menu,
                fg=color_texto,
                activebackground="#393e46",
                activeforeground="orange",
                bd=0,
                relief="flat"
            )
            for texto, funcion in items:
                if texto == "SEPARADOR":
                    menu.add_separator()
                else:
                    menu.add_command(label=texto, command=funcion)
            barraMenu.add_cascade(label=nombre, menu=menu, activebackground=COLOR_ACTIVO)

        # Menú "Inicio"
        crear_menu("Inicio", [
            ("Conectar", Primerasconeciones),
            ("Salir", SalirApp)
        ])

        # Menú "Registro"
        crear_menu("Registro", [
            ("Nuevo", funNuevo),
            ("Guardar", Func_Guardar),
            ("Actualizar", Func_Actualizar),
            ("Crear Ticket", crearticket),            
            ("Eliminar", Func_Delete)
        ])

        # Menú "Movimientos"
        crear_menu("Movimientos", [
            ("Primero", FunPrimerRegistro),
            ("Siguiente", funSiguiente),
            ("Anterior", funAnterior),
            ("Ultimo", FunUltimoRegistro)
        ])

        # Menú "Busqueda"
        crear_menu("Busqueda", [
            ("Por Email", busquedaxemail),
            ("Por Codigo", busquedaxcodigo),
            ("SEPARADOR", None),
            ("Por Cedula", busquedaxcedula),
            ("SEPARADOR", None),
            ("Por Telefono", busquedaxtelefono)
        ])

        # Menú "Ayuda"
        crear_menu("Ayuda...", [
            ("Acerca de...", msjinfo)
        ])      
        
    #::::::::::::::::::::::::::::Aqui termina el menu desplegable:::::::::::::::::::::::::::::::::
    #Cajas de texto
        # --- Entradas y etiquetas SOLO para las variables principales, reorganizadas en 4 columnas de 4 campos cada una ---
        # Usar grid con sticky y expandir columnas para que se adapten al maximizar
        for i in range(8):
            Frame1.grid_columnconfigure(i, weight=1)
        for i in range(6):
            Frame1.grid_rowconfigure(i, weight=1)

        campos = [
            ("Codigo", self.Codigo),
            ("Nombre", self.Nombre),
            ("telefono", self.telefono),
            ("Descripcion", self.Descripcion),
            ("Marca", self.Marca),
            ("Modelo", self.Modelo),
            ("Serial", self.Serial),
            ("Trab_a_real", self.Trab_a_real),
            ("Fecha_ing", self.Fecha_ing),
            ("trab_real", self.trab_real),
            ("Fecha_ent", self.Fecha_ent),
            ("Falla", self.Falla),
            ("Detalles", self.Detalles),
            ("Estado", self.Estado),
            ("Conclusion", self.Conclusion),
            ("Estadofinal", self.Estadofinal)
        ]
        for idx, (label, var) in enumerate(campos):
            row = idx % 4
            col = (idx // 4) * 2  # 0,2,4,6 para 4 columnas
            Ctk.CTkLabel(Frame1, text=label, width=20, anchor="e", justify="right").grid(row=row, column=col, padx=5, pady=3, sticky="e")
            if 'Fecha' in label:
                entry = DateEntry(Frame1, date_pattern="dd/MM/yyyy", width=17, textvariable=var)
            else:
                entry = Ctk.CTkEntry(Frame1, border_color="teal", textvariable=var)
            entry.grid(row=row, column=col+1, padx=5, pady=3, sticky="ew")

        # Subir los botones justo debajo de las cajas de texto, más anchos y más hacia arriba
        for i in range(7):
            Frame1.grid_columnconfigure(i, weight=1)
        btn_width = 80  # Más ancho
        btn_height = 36

        # Cargar imágenes (ajusta las rutas a tus archivos de imagen)
        img_nuevo = Ctk.CTkImage(light_image=Image.open("./img/nuevo.png"), dark_image=Image.open("./img/nuevo.png"), size=(24,24))
        img_guardar = Ctk.CTkImage(light_image=Image.open("./img/guardar2.png"), dark_image=Image.open("./img/guardar2.png"), size=(24,24))
        img_actualizar = Ctk.CTkImage(light_image=Image.open("./img/editar.png"), dark_image=Image.open("./img/datos.png"), size=(24,24))
        img_monitor = Ctk.CTkImage(light_image=Image.open("./img/datos.png"), dark_image=Image.open("./img/datos.png"), size=(24,24))
        img_limpiar = Ctk.CTkImage(light_image=Image.open("./img/datos.png"), dark_image=Image.open("./img/datos.png"), size=(24,24))
        img_certificado = Ctk.CTkImage(light_image=Image.open("./img/datos.png"), dark_image=Image.open("./img/datos.png"), size=(24,24))
        img_excel = Ctk.CTkImage(light_image=Image.open("./img/datos.png"), dark_image=Image.open("./img/datos.png"), size=(24,24))
       # Botones con imágenes
        btn1 = Ctk.CTkButton(Frame1, fg_color="teal", text="Nuevo", width=btn_width, height=btn_height, image=img_nuevo, compound="left", command=funNuevo)
        btn1.grid(row=4, column=0, padx=10, pady=(10, 2), sticky="ew", columnspan=1)
        btn2 = Ctk.CTkButton(Frame1, fg_color="teal", text="Guardar", width=btn_width, height=btn_height, image=img_guardar, compound="left", command=Func_Guardar)
        btn2.grid(row=4, column=1, padx=10, pady=(10, 2), sticky="ew", columnspan=1)
        btn3 = Ctk.CTkButton(Frame1, fg_color="teal", text="Actualizar", width=btn_width, height=btn_height, image=img_actualizar, compound="left", command=Func_Actualizar)
        btn3.grid(row=4, column=2, padx=10, pady=(10, 2), sticky="ew", columnspan=1)
        btn4 = Ctk.CTkButton(Frame1, fg_color="teal", text="Monitor", width=btn_width, height=btn_height, command=CargarData, image=img_monitor, compound="left")
        btn4.grid(row=4, column=3, padx=10, pady=(10, 2), sticky="ew", columnspan=1)
        btn5 = Ctk.CTkButton(Frame1, fg_color="teal", text="Limpiar", width=btn_width, height=btn_height, command=flimpiar, image=img_limpiar, compound="left")
        btn5.grid(row=4, column=4, padx=10, pady=(10, 2), sticky="ew", columnspan=1)


# ...existing code...
                # ... después de los botones principales y antes de Frame2.pack() ...

        # --- Botones de navegación (pequeños, en forma de triángulo) ---
        nav_frame = Ctk.CTkFrame(self.wind, fg_color="transparent")
        nav_frame.pack(pady=(0, 0))

        btn_nav_primero = Ctk.CTkButton(
            nav_frame, text="⏮", width=40, height=32, fg_color="teal", font=("Arial", 16),
            command=FunPrimerRegistro
        )
        btn_nav_primero.grid(row=0, column=0, padx=5)

        btn_nav_anterior = Ctk.CTkButton(
            nav_frame, text="◀", width=40, height=32, fg_color="teal", font=("Arial", 16),
            command=funAnterior
        )
        btn_nav_anterior.grid(row=0, column=1, padx=5)

        btn_nav_siguiente = Ctk.CTkButton(
            nav_frame, text="▶", width=40, height=32, fg_color="teal", font=("Arial", 16),
            command=funSiguiente
        )
        btn_nav_siguiente.grid(row=0, column=2, padx=5)

        btn_nav_ultimo = Ctk.CTkButton(
            nav_frame, text="⏭", width=40, height=32, fg_color="teal", font=("Arial", 16),
            command=FunUltimoRegistro
        )
        btn_nav_ultimo.grid(row=0, column=3, padx=5)
        # Subir el Treeview y los scrolls, expandible
        Frame2.pack(fill="both", expand=True, padx=20, pady=10)
        treeScroll = ttk.Scrollbar(Frame2,orient="vertical")
        treeScroll.pack(side="right",fill="y")
        treeScrollx = ttk.Scrollbar(Frame2,orient="horizontal")
        treeScrollx.pack(side= "bottom",fill="x")
        self.trv = ttk.Treeview(Frame2, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), show="headings", height="12", yscrollcommand=treeScroll.set, xscrollcommand=treeScrollx.set)
        self.trv.pack(fill="both", expand=True)

        # Encabezados del Treeview con los nombres de las variables
        self.trv.heading(1, text="Codigo")
        self.trv.heading(2, text="Nombre")
        self.trv.heading(3, text="telefono")
        self.trv.heading(4, text="Descripcion")
        self.trv.heading(5, text="Marca")
        self.trv.heading(6, text="Modelo")
        self.trv.heading(7, text="Serial")
        self.trv.heading(8, text="Trab_a_real")
        self.trv.heading(9, text="Fecha_ing")
        self.trv.heading(10, text="trab_real")
        self.trv.heading(11, text="Fecha_ent")
        self.trv.heading(12, text="Falla")
        self.trv.heading(13, text="Detalles")
        self.trv.heading(14, text="Estado")
        self.trv.heading(15, text="Conclusion")
        self.trv.heading(16, text="Estadofinal")
        
        self.trv.column(1, stretch=YES, anchor="center")
        self.trv.column(2, stretch=YES, anchor="center")
        self.trv.column(3, stretch=YES, anchor="center")
        self.trv.column(4, stretch=YES, anchor="center")
        self.trv.column(5, stretch=YES, anchor="center")
        self.trv.column(6, stretch=YES, anchor="center")
        self.trv.column(7, stretch=YES, anchor="center")
        self.trv.column(8, stretch=YES, anchor="center")
        self.trv.column(9, stretch=YES, anchor="center")
        self.trv.column(10, stretch=YES, anchor="center")
        self.trv.column(11, stretch=YES, anchor="center")
        self.trv.column(12, stretch=YES, anchor="center")
        self.trv.column(13, stretch=YES, anchor="center")
        self.trv.column(14, stretch=YES, anchor="center")
        self.trv.column(15, stretch=YES, anchor="center")
        self.trv.column(16, stretch=YES, anchor="center")







        # ...ajusta los valores según tus necesidades...

        self.trv.bind("<ButtonRelease-1>", traineeInfo)
        cursores=["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]

        treeScroll.config(command= self.trv.yview)
        treeScrollx.config(command=self.trv.xview,cursor="arrow")
        CargarData()




if __name__ == '__main__':
    # Prevenir múltiples instancias usando un socket local
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 65432))  # Puerto fijo para la app
    except OSError:
        tk.Tk().withdraw()
        messagebox.showerror("Advertencia", "La aplicación ya está en ejecución.")
        sys.exit(0)

    root = Ctk.CTk()
    root.wm_attributes("-topmost", 1)
    # Cargar el archivo de imagen desde el disco
    #icono = tk.PhotoImage(file="./img/libros.png",format="png")

    # Establecerlo como ícono de la ventana
    #root.iconphoto(True, icono)
    root.minsize(width=1024,height=600)
    Contratista =Contratista(root)
    root.attributes('-fullscreen')
    root.mainloop()
    # Liberar el socket al cerrar
    sock.close()