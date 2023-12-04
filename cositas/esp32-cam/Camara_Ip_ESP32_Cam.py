import cv2

url='http://192.168.137.94/640x480.jpg'
cap = cv2.VideoCapture(url) # Crear objeto VideoCapture

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while(1):
    
    cap.open(url) # Antes de capturar el frame abrimos la url
    
    ret,frame = cap.read() # Captura de frame
    
    
    #frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    #gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow(winName,frame)
    
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
     
cv2.destroyAllWindows()
