import cv2

webcam = cv2.VideoCapture(2)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video da Webcam", frame)
        key = cv2.waitKey(5)
        if key == 27: # ESC
            break
    cv2.imwrite("FotoLira.png", frame)

webcam.release()
cv2.destroyAllWindows()