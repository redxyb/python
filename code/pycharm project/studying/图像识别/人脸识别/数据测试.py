import cv2

#capture = cv2.VideoCapture(0)
# minW = 0.1*capture.get(3)
# minH = 0.1*capture.get(4)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
frame = cv2.imread("liudehua2.jpg")
    # 将使用的图片转换为灰度照片，opencv人脸检测器只能使用灰度图像
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 加载opencv的人脸检测分类器
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 检测多尺度图片，返回值是一张脸部区域信息的列表（x,y,宽，高）
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
(x, y, w, h) = faces[0]

for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    idnum, confidence = recognizer.predict(gray[y:y + h, x:x + w])

    if confidence <= 50:
        cv2.putText(frame, "xyb", (x + 5, y - 5), font, 1, (0, 0, 255), 1)
    else:
        cv2.putText(frame, "unknown", (x + 5, y - 5), font, 1, (0, 0, 255), 1)
cv2.imshow("video", frame)
cv2.waitKey(0)
cv2.destroyWindow(1)#释放资源