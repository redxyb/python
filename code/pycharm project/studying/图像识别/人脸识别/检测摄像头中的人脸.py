import cv2

capture = cv2.VideoCapture(0)
fd = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = capture.read()  #read()返回 （bool（是否有图片, 当前获取的一帧数据）
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    #灰化处理
    faces = fd.detectMultiScale(gray,1.2,5)
    for l, t, w, h in faces:
        cv2.ellipse(frame, (l + int(w / 2), t + int(h / 2)), (int(w / 2), int(h / 2)), 0, 0, 360, (0, 255, 0), 2)
        #face = frame[t:t + h, l:l + w]
        cv2.putText(frame, "xiaoyuebin", (int(w / 2), int(h / 2)), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 0), 2)
    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xff == ord("q"):   #延时10ms，按下q退出
        break
cv2.destroyWindow()#释放资源