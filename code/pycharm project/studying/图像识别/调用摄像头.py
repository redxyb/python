import cv2
'''通过摄像头显示自己的视频，并对自己的视频旋转40度输出 
（拓展：输出视频的分辨率为240*340，每秒帧率24-30帧）'''
capture = cv2.VideoCapture(0)#可放入视频文件
framecount = 0

while framecount != 26:#设置采集帧数为26次
    ret,frame = capture.read()#read()返回值有两个，第一个是bool，代表有没有获取到图像；第二个是当前获取的一帧图像
    framecount += 1
    #frame = cv2.flip(frame,1)#图像翻转：0代表上下翻转，大于0水平翻转
    #w, h = frame.shape
    h , w = 240 , 340
    rotate = cv2.getRotationMatrix2D((w / 2, h / 2), 40, 1)
    after_rotate = cv2.warpAffine(frame, rotate, (w, h))
    if not ret:
        break
    cv2.imshow("video",after_rotate)
    if cv2.waitKey(1000) & 0xFF == ord("q"):#设置采集时间为1s
        break
cv2.destroyWindow()#释放资源