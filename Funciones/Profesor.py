from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import os, io
from google.cloud import vision
from google.cloud.vision import types

# Codigo propiedad del profesor Leonardo Viquez #
# pequeñas modificaciones hechas a la original #
########################################################################################################################
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'
client = vision.ImageAnnotatorClient()

def reconocer_caras(url):
    with io.open(url, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.face_detection(image=image)

    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('0%', '1%', '25%', '50%', '75%', '100%')

    # lista simplificada de rostros con datos simplificados
    faces_list = []
    for face in faces:
        # dicccionario con los angulos asociados a la detección de la cara
        face_angles = dict(roll_angle=face.roll_angle, pan_angle=face.pan_angle, tilt_angle=face.tilt_angle)

        # confianza de detección (tipo float)
        detection_confidence = face.detection_confidence

        # Probabilidad de Expresiones
        face_expressions = dict(joy_likelihood=likelihood_name[face.joy_likelihood],
                                sorrow_likelihood=likelihood_name[face.sorrow_likelihood],
                                anger_likelihood=likelihood_name[face.anger_likelihood],
                                surprise_likelihood=likelihood_name[face.surprise_likelihood],
                                under_exposed_likelihood=likelihood_name[face.under_exposed_likelihood],
                                blurred_likelihood=likelihood_name[face.blurred_likelihood],
                                headwear_likelihood=likelihood_name[face.headwear_likelihood])

        # polígono de marco de cara
        vertices = []
        for vertex in face.bounding_poly.vertices:
            vertices.append(dict(x=vertex.x, y=vertex.y))

        face_dict = dict(face_angles=face_angles,
                         detection_confidence=detection_confidence,
                         face_expressions=face_expressions,
                         vertices=vertices
                         )
        faces_list.append(face_dict)
    # retorna lista de objetos con características del reconocimiento facial
    return faces_list


def seleccionar_imagen():
    root = Tk()
    root.title('Seleccionar imagen')
    root.geometry('300x0')

    root.filename = filedialog.askopenfile(initialdir="/", title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    try:
        root.destroy()
    except:
        pass
    try:
        return (root.filename.name)
    except:
        return
def detector_de_caras():
    root = Tk()
    root.title('canvas')

    root.filename = filedialog.askopenfile(initialdir="/", title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    # print (root.filename.name)

    scrollbary = Scrollbar(root)
    scrollbary.pack(side=RIGHT, fill=Y)

    scrollbarx = Scrollbar(root, orient=HORIZONTAL)
    scrollbarx.pack(side=BOTTOM, fill=X)

    # circulo
    canvas = Canvas(width=400, height=400, bg='white', xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    canvas.pack(expand=YES, fill=BOTH)

    scrollbary.config(command=canvas.yview)
    scrollbarx.config(command=canvas.xview)

    ##img = PhotoImage(file="flor.jpg")
    img = ImageTk.PhotoImage(Image.open(root.filename.name))
    canvas.create_image(0, 0, anchor=NW, image=img)

    canvas.create_rectangle(200, 132, 516, 606, width=5, fill='red', stipple="gray12")

    root.mainloop()
########################################################################################################################
