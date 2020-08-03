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
                return data
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            return
