import cv2

capture = cv2.VideoCapture(0)
minW = 0.1*capture.get(3)
minH = 0.1*capture.get(4)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
idnum = 0
names = ['xiaoyuebin']

while True:
    ret, frame = capture.read()  #read()返回 （bool（是否有图片, 当前获取的一帧数据）
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    #灰化处理
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        idnum, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if confidence <= 70:
            idnum = names[idnum]
        else:
            idnum = "unknown"
        cv2.putText(frame, str(idnum), (x + 5, y - 5), font, 1, (0, 0, 255), 1)
    cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyWindow(1)#释放资源