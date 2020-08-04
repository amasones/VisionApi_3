from tkinter import *
from Funciones.Camara import tomar_foto
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog


class Ventana_Registro:
    def __init__(self, ven):
        self.root = ven
        ven.title("Reconocimiento de Rostros")
        ven.configure(bg='beige')  # Color de fondo
        self.titulo = Label(ven, text='Elija una opción', bg='beige', font=('Helvetica', 21))
        self.titulo.grid(column=0, row=0, columnspan=4, pady=10)

        self.boton_foto = Button(ven, text='Tomar una foto\ndesde webcam', height=2, width=16,font=('Helvetica', 21)
                                        ,command=sub_tomar_foto).\
                                        grid(column=0, row=1, pady=5, padx=5, columnspan=2)

        self.boton_seleccionar = Button(ven, text='Seleccionar una foto\ndesde el equipo', height=2, width=16,
                                        font=('Helvetica', 21),command=None).\
                                        grid(column=2, row=1, pady=5, padx=5, columnspan=2)

class SubVentana_Foto:
    def __init__(self, ven):
        self.root = ven
        ven.title("Tomar Foto")
        ven.withdraw()
        ven.configure(bg='beige')  # Color de fondo
        instrucciones=messagebox.showinfo(message="Precione espacio para capturar la foto",
                                          title="Instrucciones")
        self.foto()

    def foto(self):
        confirmar=tomar_foto()
        if confirmar is None:
            pass
        else:
            mensaje_confirmar = messagebox.askyesno(message="¿Desea enviar esta foto?",
                                                    title="Confirmacion")
            if mensaje_confirmar is True:
                pass
            else:
                self.foto()



def ventana_registro():
    root = Toplevel()
    v_registro = Ventana_Registro(root)

def sub_tomar_foto():
    root = Toplevel()
    v_foto = SubVentana_Foto(root)