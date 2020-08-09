# Github: https://github.com/amasones/VisionApi_3

import tkinter as tk

from Ventanas.Registro import ventana_registro
from Ventanas.Reportes import ventana_reporte


class Menu_Interfaz:
    def __init__(self, ven):
        self.raiz = ven  # Iniciador del GUI
        ven.configure(bg='beige')  # Color de fondo
        ven.title('Vision API 3: End of suffering')  # Título del programa

        self.titulo = tk.Label(ven, text='Google Vision API', bg='beige', font=('Helvetica', 21))
        self.titulo.grid(column=0, row=0, columnspan=4, pady=10)

        self.boton_registro = tk.Button(ven, text='Registro\nde\nasistencia', height=5, width=15, font=('Helvetica', 21)
                                        , command=ventana_registro).grid(column=0, row=1, pady=5, padx=20, columnspan=2)
        self.boton_reporte = tk.Button(ven, text='Ver reportes', height=2, width=15, font=('Helvetica', 21)
                                       , command=ventana_reporte).grid(column=0, row=2, pady=15, padx=20, columnspan=2)
        self.boton_salir = tk.Button(ven, text='Salir del programa', height=2, width=15, font=('Helvetica', 21)
                                     , command=None).grid(column=0, row=3, pady=15, padx=20, columnspan=2)


raiz = tk.Tk()
menu = Menu_Interfaz(raiz)
raiz.mainloop()
