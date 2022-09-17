from cvzone.FaceDetectionModule import FaceDetector
import cv2
cap=cv2.VideoCapture(2)
detector=FaceDetector()
while True:
    ret,frame=cap.read()
    frame,bboxs=detector.findFaces(frame)
    frame=cv2.flip(frame,-1)
    frame=cv2.flip(frame,1)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
