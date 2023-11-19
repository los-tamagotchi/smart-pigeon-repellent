import cv2

url = 'http://192.168.0.31/cam-hi.jpg'
cap = cv2.VideoCapture(url)

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while(True):
    cap.open(url)

    ret, frame = cap.read()

    if ret:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(winName, frame)
        tecla = cv2.waitKey(1) & 0xFF

    if (tecla == 27):
        break

cv2.destroyAllWindows()
