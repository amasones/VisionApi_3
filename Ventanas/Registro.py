from tkinter import *
from tkinter import messagebox

from Funciones.Camara import tomar_foto
from Funciones.Rostros import procesar_rostro, procesar_cargado
from Main import *

class Ventana_Registro:
    def __init__(self, ven):
        self.root = ven
        ven.title("Reconocimiento de Rostros")
        ven.configure(bg='beige')  # Color de fondo
        self.titulo = Label(ven, text='Elija una opción', bg='beige', font=('Helvetica', 21))
        self.titulo.grid(column=0, row=0, columnspan=4, pady=10)

        self.boton_foto = Button(ven, text='Tomar una foto\ndesde webcam', height=2, width=16, font=('Helvetica', 21)
                                 , command=sub_tomar_foto).grid(column=0, row=1, pady=5, padx=5, columnspan=2)

        self.boton_seleccionar = Button(ven, text='Seleccionar una foto\ndesde el equipo', height=2, width=16,
                font=('Helvetica', 21), command=sub_cargar_imagen).grid(column=2, row=1, pady=5,padx=5, columnspan=2)

        self.boton_siguiente = Button(ven, text='Siguiente', height=2, width=16,font=('Helvetica', 21),
                                  command=None).grid(column=0, row=2, pady=5, padx=5, columnspan=4)


class SubVentana_Foto:
    def __init__(self, ven):
        self.root = ven
        ven.withdraw()
        messagebox_info("Presione espacio para tomar la foto", "Instucciones")
        self.foto()

    def foto(self):
        confirmar = tomar_foto()
        if confirmar is None:
            pass
        else:
            mensaje_confirmar = messagebox.askyesno(message="¿Desea enviar esta foto?",
                                                    title="Confirmacion")
            if mensaje_confirmar is True:
                datos = procesar_rostro()
                archi = open("Datos/foto.dat", "w")
                archi.write(str(datos))
                archi.close()
                messagebox_info("La foto ha sido procesada", "Listo")
                return
            else:
                self.foto()


class SubVentana_Cargar:
    def __init__(self, ven):
        self.root = ven
        ven.withdraw()
        self.cargar()

    def cargar(self):
        datos = procesar_cargado()
        archi = open("Datos/foto.dat", "w")
        archi.write(str(datos))
        archi.close()
        messagebox_info("La foto ha sido procesada", "Listo")


class SubVentana_Siguiente:
    def __init__(self, ven):
        self.root = ven
        ven.title("Informacion")
        ven.configure(bg='beige')  # Color de fondo
        

def ventana_registro():
    root = Toplevel()
    Ventana_Registro(root)
    return


def sub_tomar_foto():
    root = Toplevel()
    SubVentana_Foto(root)
    return


def sub_cargar_imagen():
    root = Toplevel()
    SubVentana_Cargar(root)
    return

def sub_siguiente():
    archi = open("Datos/foto.dat", "r")
    lista = archi.read()
    lista = eval(lista)


def messagebox_info(mensaje, titulo):
    messagebox.showinfo(message=str(mensaje), title=str(titulo))
    return

