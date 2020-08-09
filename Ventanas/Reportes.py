from tkinter.tix import *

from Ventanas.Registro import cursos


class Ventana_Reportes:
    def __init__(self, ven):
        self.root = ven
        ven.title("Reportes")  # titulo de la ventana
        ven.configure(bg='beige')  # Color de fondo
        self.instrucciones = Label(ven, text='Elija una opción', bg='beige', font=('Helvetica', 21)). \
            grid(column=0, row=0, columnspan=4, pady=10)  # Label con instrucciones

        self.boton_asistencia = Button(ven, text='Registro de asistencia\n por estudiantes', height=2, width=21,
                                       font=('Helvetica', 21), command=subventana_asistencia) \
            .grid(column=0, row=1, pady=15, padx=20, columnspan=2)
        self.boton_fecha = Button(ven, text='Estado de emociones\npor fecha para un curso', height=2, width=21,
                                  font=('Helvetica', 21), command=subventana_emociones) \
            .grid(column=0, row=2, pady=15, padx=20, columnspan=2)
        self.boton_promedio = Button(ven, text='Promedio de emociones\npor un estudiante en curso', height=2, width=21,
                                     font=('Helvetica', 21), command=subventana_estudiantes) \
            .grid(column=0, row=3, pady=15, padx=20, columnspan=2)


class SubVentana_Asistencia:
    matriz = []
    total_horizontal = 0
    total_vertical = 0

    def __init__(self, ven):
        self.root = ven
        self.hacer_matriz()
        ven.title("Reportes")  # titulo de la ventana
        ven.configure(bg='beige')  # Color de fondo

        for x in range(self.total_horizontal):
            for y in range(self.total_vertical):
                self.tabla = Entry(ven, width=20, font=('Helvetica', 16, 'bold'))
                self.tabla.grid(row=x, column=y + 1)
                self.tabla.insert(END, self.matriz[x][y])

    def hacer_matriz(self):
        self.matriz = [("Fecha", "Identificaion", "Emoción más relevante")]
        for x in cursos:
            self.matriz.append(x.devolver_tabla)
        print(self.matriz)

        self.total_horizontal = len(self.matriz)
        self.total_vertical = len(self.matriz[0])


class SubVentana_Emociones:
    """
    Genuinamente no quiero documentar el desastre que hice acá, entonces buena suerte tratando de decifrarlo
    """
    matriz = []
    total_horizontal = 0
    total_vertical = 0

    def __init__(self, ven):
        self.root = ven
        self.hacer_matriz()
        ven.title("Reportes")  # titulo de la ventana
        ven.configure(bg='beige')  # Color de fondo

        for x in range(self.total_horizontal):
            for y in range(self.total_vertical):
                self.tabla = Entry(ven, width=20, font=('Helvetica', 16, 'bold'))
                self.tabla.grid(row=x, column=y + 1)
                self.tabla.insert(END, self.matriz[x][y])

    def hacer_matriz(self):
        self.matriz = [("Curso", "Fecha", "Emoción", "Porcentaje")]
        fecha_y_materia = []
        lista_temporal = []
        felicidad = []
        triste = []
        enojo = []
        sorpresa = []

        for x in cursos:
            if (x.devolver_fecha(), x.devolver_curso()) not in fecha_y_materia:
                fecha_y_materia.append([x.devolver_curso(), x.devolver_fecha()])

        for x in cursos:
            felicidad.append((x.devolver_curso(), x.devolver_fecha(), x.devolver_felicidad()))
            triste.append((x.devolver_curso(), x.devolver_fecha(), x.devolver_tristeza()))
            enojo.append((x.devolver_curso(), x.devolver_fecha(), x.devolver_enojo()))
            sorpresa.append((x.devolver_curso(), x.devolver_fecha(), x.devolver_sorpresa()))

        try:
            porcentaje = 0
            cantidad = 0
            for x in felicidad:
                if [x[0], x[1]] in fecha_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Felicidad:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        try:
            porcentaje = 0
            cantidad = 0
            for x in triste:
                if [x[0], x[1]] in fecha_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Trizteza:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        try:
            porcentaje = 0
            cantidad = 0
            for x in enojo:
                if [x[0], x[1]] in fecha_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Enojo:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        try:
            porcentaje = 0
            cantidad = 0
            for x in sorpresa:
                if [x[0], x[1]] in fecha_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Sorpresa:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        self.total_horizontal = len(self.matriz)
        self.total_vertical = len(self.matriz[0])


class SubVentana_Estudiantes:
    """
    Genuinamente no quiero documentar el desastre que hice acá, entonces buena suerte tratando de decifrarlo
    """
    matriz = []
    total_horizontal = 0
    total_vertical = 0

    def __init__(self, ven):
        self.root = ven
        self.hacer_matriz()
        ven.title("Reportes")  # titulo de la ventana
        ven.configure(bg='beige')  # Color de fondo

        for x in range(self.total_horizontal):
            for y in range(self.total_vertical):
                self.tabla = Entry(ven, width=20, font=('Helvetica', 16, 'bold'))
                self.tabla.grid(row=x, column=y + 1)
                self.tabla.insert(END, self.matriz[x][y])

    def hacer_matriz(self):
        self.matriz = [("Cédula", "Curso", "Emoción", "Porcentaje")]
        cedula_y_materia = []
        lista_temporal = []
        felicidad = []
        triste = []
        enojo = []
        sorpresa = []

        for x in cursos:
            if (x.devolver_cedula, x.devolver_curso()) not in cedula_y_materia:
                cedula_y_materia.append([x.devolver_cedula(), x.devolver_curso()])

        for x in cursos:
            felicidad.append((x.devolver_cedula(), x.devolver_curso(), x.devolver_felicidad()))
            triste.append((x.devolver_cedula(), x.devolver_curso(), x.devolver_tristeza()))
            enojo.append((x.devolver_cedula(), x.devolver_curso(), x.devolver_enojo()))
            sorpresa.append((x.devolver_cedula(), x.devolver_curso(), x.devolver_sorpresa()))

        try:
            porcentaje = 0
            cantidad = 0
            for x in felicidad:
                if [x[0], x[1]] in cedula_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Felicidad:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        try:
            porcentaje = 0
            cantidad = 0
            for x in triste:
                if [x[0], x[1]] in cedula_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Trizteza:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        try:
            porcentaje = 0
            cantidad = 0
            for x in enojo:
                if [x[0], x[1]] in cedula_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Enojo:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        try:
            porcentaje = 0
            cantidad = 0
            for x in sorpresa:
                if [x[0], x[1]] in cedula_y_materia:
                    porcentaje = porcentaje + x[2]
                    lista_temporal = (x[0], x[1])
                    cantidad += 1
            porcentaje = porcentaje / cantidad
            self.matriz.append((lista_temporal[0], lista_temporal[1], "Sorpresa:", porcentaje))
        except (IndexError, ZeroDivisionError):
            pass

        self.total_horizontal = len(self.matriz)
        self.total_vertical = len(self.matriz[0])


def ventana_reporte():
    root = Toplevel()
    Ventana_Reportes(root)
    return


def subventana_asistencia():
    root = Toplevel()
    SubVentana_Asistencia(root)
    return


def subventana_emociones():
    root = Toplevel()
    SubVentana_Emociones(root)
    return


def subventana_estudiantes():
    root = Toplevel()
    SubVentana_Estudiantes(root)
    return
