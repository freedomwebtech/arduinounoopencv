from cvzone.FaceDetectionModule import FaceDetector
import cv2
import serial,time

cap = cv2.VideoCapture(0)
detector = FaceDetector()
ArduinoSerial=serial.Serial('/dev/ttyACM0',9600)

while True:
    success, img = cap.read()
    img=cv2.flip(img,-1)

    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        string='X{0:d}'.format((center[0]-70))
        ArduinoSerial.write(string.encode('utf-8'))
        
            
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()