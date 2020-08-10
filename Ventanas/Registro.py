from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import os

from Funciones.Camara import tomar_foto, detector_qr
from Funciones.Rostros import procesar_rostro, procesar_cargado

cursos = []  # Se almacenará direcciones de memoria


class Asistencia:
    """
    Se usa solo para asignar valores y retornarlos si se ocupan
    """
    curso = None
    identificacion = None
    emociones = None
    fecha = None

    def asignar_datos(self, curso, identificacion, emociones, fecha):
        self.curso = curso
        self.identificacion = identificacion
        self.emociones = emociones
        self.fecha = fecha
        return

    def devolver_diccionario(self):
        return {self.curso: (self.identificacion, self.emociones, self.fecha)}

    @property
    def devolver_tabla(self):
        espanol = ["Felicidad", "Tristeza", "Enojo", "Sorpresa"]
        ingles = ["joy", "sorrow", "anger", "surpris"]
        comparador = 0
        for x in self.emociones:
            if x[1] > comparador:
                lista = x
                comparador = x[1]
            else:
                pass
        formato = lista[0].strip("_likelihood")
        if formato in ingles:
            formato = espanol[ingles.index(formato)]
        formato = formato + " = " + str(lista[1])
        return self.fecha[0], self.identificacion, formato

    def devolver_felicidad(self):
        return self.emociones[0][1]

    def devolver_tristeza(self):
        return self.emociones[1][1]

    def devolver_enojo(self):
        return self.emociones[2][1]

    def devolver_sorpresa(self):
        return self.emociones[3][1]

    def devolver_curso(self):
        return self.curso

    def devolver_fecha(self):
        return self.fecha[0]

    def devolver_cedula(self):
        return self.identificacion


class Ventana_Registro:
    def __init__(self, ven):
        """
        Muestra 4 funciones:
        "Tomar una foto desde webcam" accede a la cámara del computador, toma una foto, y la guarda en Datos/foto.png
        "Seleccionar una imagen desde el equipo" guarda la dirección de la foto en memoria
        "Siguiente" Abre una ventana extra en la que el usuario digita información adicional
        "Guardar y volver al menú" Guarda la dirección de memoria en una lista y destruye archivos creados temporales
        :param ven: Necesita que el parametro anteriormente tenga el atributo Toplevel() para accesar interfaz
        """
        self.root = ven
        ven.title("Reconocimiento de Rostros")  # titulo de la ventana
        ven.configure(bg='beige')  # Color de fondo
        self.instrucciones = Label(ven, text='Elija una opción', bg='beige', font=('Helvetica', 21)). \
            grid(column=0, row=0, columnspan=4, pady=10)  # Label con instrucciones

        self.boton_foto = Button(ven, text='Tomar una foto\ndesde webcam', height=2, width=16, font=('Helvetica', 21)
                                 , command=sub_tomar_foto) \
            .grid(column=0, row=1, pady=5, padx=5, columnspan=2)
        self.boton_seleccionar = Button(ven, text='Seleccionar una foto\ndesde el equipo', height=2, width=16,
                                        font=('Helvetica', 21), command=sub_cargar_imagen) \
            .grid(column=2, row=1, pady=5, padx=5, columnspan=2)

        self.boton_siguiente = Button(ven, text='Siguiente', height=2, width=16, font=('Helvetica', 21),
                                      command=sub_siguiente) \
            .grid(column=0, row=2, pady=5, padx=5, columnspan=4)
        self.boton_guardar = Button(ven, text='Guardar y volver al menú', height=2, width=20, font=('Helvetica', 21),
                                    command=self.salir) \
            .grid(column=0, row=3, pady=15, padx=5, columnspan=4)

    def salir(self):
        """
        Guarda los datos en una lista con memorias y elimina: foto.png, foto.dat, registro.dat(En la carpeta Datos)
        :return:
        """
        try:
            sub_guardar()
            os.remove("Datos/foto.png")
            os.remove("Datos/foto.dat")
            os.remove("Datos/registro.dat")
            self.root.destroy()

        except FileNotFoundError:
            messagebox_info("Falta informacion por llenar", "Error")
            print(cursos)
        return


class SubVentana_Foto:
    """
    Toma una foto desde la webcam y la procesa mediante Google Vision, por ultimo lo guarda en el archivo "foto.dat"
    """

    def __init__(self, ven):
        self.root = ven
        ven.withdraw()  # Hace que la ventana no aparezca
        messagebox_info("Presione espacio para tomar la foto", "Instucciones")
        self.foto()

    def foto(self):
        confirmar = tomar_foto()  # Cuando se toma la foto se guarda en foto.png y la funcion retorna un "si"
        if confirmar is None:  # Verifica si confirma tiene un dato, si no retorna nada (None) lo ignora y cierra
            pass
        else:
            mensaje_confirmar = messagebox.askyesno(message="¿Desea enviar esta foto?", title="Confirmacion")
            if mensaje_confirmar is True:  # API Vision procesa la foto y se asignan los resultados en foto.dat
                datos = procesar_rostro()
                guardar_archivo("Datos/foto.dat", datos)
                messagebox_info("La foto ha sido procesada", "Listo")
                return
            else:
                self.foto()  # Vuelve a tomar la foto


class SubVentana_Cargar:
    """
    Agarra una direccion en el equipo donde esté almacenada una foto, la procesa la API y la escribe en foto.dat
    """

    def __init__(self, ven):
        self.root = ven
        ven.withdraw()
        self.cargar()

    @staticmethod
    def cargar():
        datos = procesar_cargado()
        guardar_archivo("Datos/foto.dat", datos)
        messagebox_info("La foto ha sido procesada", "Listo")


class SubVentana_Siguiente:
    def __init__(self, ven):
        """
        En esta ventana hay 2 datos por llenar, la cedula y el curso, la cedula es un entrybox simple, el curso usa un
        combobox para asegurar que no ingrese un curso no existente (todos los cursos existentes estan en
        self.lista_cursos. Luego está la opcion "Cargar código QR" que activa la camara y retorna una lista
        ( ["cedula","curso"] ) y los asigna en cedula y curso respectivamente.
        Por otro lado self.entrada(cedula) y self.entrada2(curso) sirve como StringVar, o sea que permiten el agarre de
        datos de las entradas, ya que por alguna razón el .get no sirve en el self.entry_cedula y self.box_curso (aunque
        deberían de) entonces la solución es asignarlos con un textvariable=self.entrada/entrada2 para que funcionen.
        """
        self.root = ven
        ven.title("Informacion")
        ven.configure(bg='beige')

        self.lista_cursos = ["Taller50", "Intro50"]

        self.entrada = StringVar()
        self.entrada2 = StringVar()

        self.label_cedula = Label(ven, text='Cédula del estudiante:', bg='beige', font=('Helvetica', 15)) \
            .grid(column=0, row=1, columnspan=1, pady=10)
        self.label_curso = Label(ven, text='Código del curso:', bg='beige', font=('Helvetica', 15)) \
            .grid(column=0, row=2, columnspan=1, pady=10)

        self.entry_cedula = Entry(ven, font=('Helvetica', 15), textvariable=self.entrada) \
            .grid(column=1, row=1, columnspan=1, pady=10, padx=10)
        self.box_curso = ttk.Combobox(ven, font=('Helvetica', 15), values=self.lista_cursos, state="readonly",
                                      textvariable=self.entrada2) \
            .grid(column=1, row=2, columnspan=1, pady=10, padx=10)

        self.boton_qr = Button(ven, text='Cargar\ncódigo QR', height=3, width=12, font=('Helvetica', 21),
                               command=self.cargar_QR) \
            .grid(column=0, row=3, pady=10, padx=20, columnspan=1)
        self.boton_guardar = Button(ven, text='Guardar', height=2, width=12, font=('Helvetica', 21)
                                    , command=self.guardar_datos) \
            .grid(column=1, row=3, pady=10, columnspan=1)

    def guardar_datos(self):
        """
        A la hora de presionar el botón guardar, el usuario deberá ingresar su informacion, una vez hecho eso se creará
        un diccionario( "curso":["cedula",("emociones"),("fecha","hora") y se guardará en el archivo registro.dat
        """
        tiempo = datetime.datetime.now()  # Agarra la fecha y hora actual del equipo
        emociones = retornar_archivo("Datos/foto.dat")

        if self.entrada.get() == "" or self.entrada2.get() == "":
            print("Por favor llene los espacios")
            return
        dic = {self.entrada2.get(): (self.entrada.get(), emociones, (tiempo.strftime("%x"), tiempo.strftime("%X")))}
        guardar_archivo("Datos/registro.dat", dic)
        messagebox_info("Se han guardado exitosamente los datos", "Listo")
        self.root.destroy()  # Cierra la ventana de "Siguiente"
        return

    def cargar_QR(self):
        """
        lee un código QR con la siguiente informacion ("cédula","curso") y las asigna en cédula y cursos respectivamente
        """
        datos = detector_qr()
        self.entrada.set(datos[0])
        self.entrada2.set(datos[1])
        return


"""
Las siguientes funciones solo sirven para poder ser asigandas a un botón y poder abrir una ventana 
"""


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
    root = Toplevel()
    SubVentana_Siguiente(root)


def sub_guardar():
    """
    Asigna los datos en registro.dat en la clase Asistencia para ser agregados a la lista de cursos como dirección de
    memoria
    """
    datos = retornar_archivo("Datos/registro.dat")
    try:
        for x, y in datos.items():
            asignador = Asistencia()
            asignador.asignar_datos(x, y[0], y[1], y[2])
            cursos.append(asignador)
    except FileNotFoundError:
        messagebox_info("Por favor clickee en siguiente y llene los datos solicitados", "Error")
    print(cursos)
    return


def messagebox_info(mensaje, titulo):  # Muestra un mensaje de informacion
    messagebox.showinfo(message=str(mensaje), title=str(titulo))
    return


def retornar_archivo(url):  # Lee archivos en una direccion del computador
    archi = open(url, "r")
    datos = archi.readline()
    archi.close()
    return eval(datos)


def guardar_archivo(url, datos):  # Guarda archivos en una direccion del computador con datos sumistrados por el usuario
    archi = open(url, "w")
    archi.write(str(datos))
    archi.close()
    return
