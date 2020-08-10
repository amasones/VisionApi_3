from Ventanas.Registro import cursos, Asistencia


def guardar_binario():
    """
    lee las direcciones de memoria de cursos y las convierte en diccionarios y por ultimo las guarda en un archivo
    binario
    """
    lista = []
    for x in cursos:
        lista.append(x.devolver_diccionario())
    archi = open("Datos/memoria.bin", "wb")
    archi.write(bytes(str(lista), "utf8"))
    archi.close()
    return


def leer_binario():
    """Lee los datos binarios de un archivo binario"""
    archi = open("Datos/memoria.bin", "rb")
    byte = archi.readline()
    archi.close()
    return eval(byte)


def cargar_memoria():
    """
    Lee lo cargado en leer_binario, lo asigna a la clase Asistencia y devuelve las direcciones a la lista cursos
    """
    datos = leer_binario()
    print(datos)
    for z in datos:
        for x, y in z.items():
            asignador = Asistencia()
            asignador.asignar_datos(x, y[0], y[1], y[2])
            cursos.append(asignador)

    print(cursos)
    for x in cursos:
        print(x.devolver_diccionario())
    return
