import tkinter as Tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self,window):
        self.ventana1=window
        
        self.agregar_menu()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = Tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = Tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Recuperar archivo", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)  

    def salir(self):
        sys.exit()

    def guardar(self,scroll):
        self.scrolledtext1=scroll
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("gpw files","*.gpw"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", Tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def recuperar(self,scroll):
        self.scrolledtext1=scroll
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("gpw files","*.gpw"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", "end") 
            self.scrolledtext1.insert("1.0", contenido)