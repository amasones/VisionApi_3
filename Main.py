# Github: https://github.com/amasones/VisionApi_3

import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import Funciones.Camara as cam
from Ventanas.Registro import ventana_registro,Asistencia



class Menu_Interfaz:
    def __init__(self, raiz):
        self.raiz = raiz  # Iniciador del GUI
        raiz.configure(bg='beige')  # Color de fondo
        raiz.title('Vision API 3: End of suffering')  # Título del programa

        self.titulo = tk.Label(raiz, text='Google Vision API', bg='beige', font=('Helvetica', 21))
        self.titulo.grid(column=0, row=0, columnspan=4, pady=10)

        self.boton_registro = tk.Button(raiz, text='Registro\nde\nasistencia', height=5, width=15,font=('Helvetica', 21)
            ,command=ventana_registro).grid(column=0, row=1, pady=5, padx=5, columnspan=2)
        self.boton_salir = tk.Button(raiz, text='Salir del programa', height=2, width=15,font=('Helvetica', 21)
                                        ,command=None).grid(column=0, row=2, pady=5, padx=5, columnspan=2)




raiz = tk.Tk()
menu = Menu_Interfaz(raiz)
raiz.mainloop()
