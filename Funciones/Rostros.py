from Funciones.Profesor import reconocer_caras


def procesar_rostro():
    """
    Esta funcion busca en la direccion "Datos/foto.png (en el caso de que no exista solo enviará None), una vez ubicada
    la imagen se envía a la Vision API para que sea procesada y de ahí sacar una diccionario(o uno de sus items)
    "face_expressions", luego toma 4 emociones (joy,sorrow,anger,surprise) y empaca en una tupla para ser retornadas
    :return:('joy_likelihood', 'X%'),('sorrow_likelihood', 'X%'),('anger_likelihood', 'X%'),('surprise_likelihood', 'X%')
    """
    datos = (reconocer_caras("Datos/foto.png"))
    lista = []
    for x, y in datos[0].get("face_expressions").items():
        lista.append((x, y))

    felicidad = (lista[0])
    tristeza = (lista[1])
    enojo = (lista[2])
    sorpresa = (lista[3])
    return felicidad, tristeza, enojo, sorpresa
