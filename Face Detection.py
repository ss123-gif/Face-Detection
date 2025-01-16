import cv2

#alg = "haarcascade_frontalface_default.xml"
#haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

   #or

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)      #initialising camrera
while True:                    #infinite loop
    _, img = cam.read()       #reading frame from camera
    
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting color
    
    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 5) #4 faces max detect
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y + h), (0, 255, 0), 2)
    cv2.imshow("FaceDetection",img)     #display the frame
    
    key = cv2.waitKey(10)
    print(key)
    if key == ord("a"):                   #exit key
        break
cam.release()
cv2.destroyAllWindows()
    



