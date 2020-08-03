# Github: https://github.com/amasones/VisionApi_3

import datetime
import Funciones.Camara as cam
class Asistencia:
    cedula=None
    curso=None
    foto=None
    emociones=None
    fecha=None
    def __init__(self,cedula,curso):
        self.cedula=cedula
        self.curso=curso
        self.fecha= datetime.datetime.now()
        self.emociones=None
    def procesar_emociones(self):
        pass
print(cam.detector_qr())
cam.tomar_foto()