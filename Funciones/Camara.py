import cv2


def detector_qr():
    camara = cv2.VideoCapture(0)  # Activar la camara de la computadora
    detector = cv2.QRCodeDetector()  # Funcion para que detecte la imagen QR
    while True:
        _, img = camara.read()  # Permite a la camara leer
        data, bbox, _ = detector.detectAndDecode(img)  # Busca si hay un QR en la imagen
        if bbox is not None:  # Lo repite infinitamente hasta que detecte el codigo
            # lee lineas en la imagen
            for i in range(len(bbox)):
                # dibuja lineas en la imagen
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            if data:  # Lee los datos y los saca
                camara.release()
                cv2.destroyAllWindows()
                return eval(data)  # Convierte de string a diccionario o lista si es necesario

        cv2.imshow("Detector de imagenes QR", img)

        if cv2.waitKey(1) == ord("q"): # Presionar q por si acaso el asuario cambia de opinion y quiere salir
            camara.release()
            cv2.destroyAllWindows()
            return


def tomar_foto():  # Muestra una ventana con lo que ve la camara actualmente para que el usuario pueda tomarse una foto
    camara = cv2.VideoCapture(0)
    while True:
        """
        Sirve para que las personas que quieran tomar una foto antes de que la camara se haya inicializado no crasheen 
        el programa tirando un error de camara, especificamente no sé como funciona pero sirve.
        credito a derricw:
        https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv/34588758
        """
        ret, frame = camara.read()
        if not ret:
            break
        cv2.imshow("Tomar foto", frame)

        k = cv2.waitKey(1)

        if k % 256 == 32:  # Cuando se preciona espacio
            cv2.imwrite("Datos/foto.png", frame)  # Se guarda en la carpeta Datos y para que la API luego la lea
            print("Se ha capturado la imagen")
            camara.release()
            cv2.destroyAllWindows()
            # Lo anterior permite liberar la camara para que no haya problemas de bucles
            return "si"
