import cv2
import os
import numpy as np

#个人人脸数据训练采集

def detect_face(img):
    # 将使用的图片转换为灰度照片，opencv人脸检测器只能使用灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 加载opencv的人脸检测分类器
    face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # 检测多尺度图片，返回值是一张脸部区域信息的列表（x,y,宽，高）
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    # 如过未检测到面部，则返回原始图片
    if(len(faces) == 0):
        return None, None
    # 目前假设只有一张脸，xy为左上角的坐标，wh为矩形的高
    (x, y, w, h) = faces[0]

    # 返回图像正面部分
    return gray[y:y+w, x:x+h], faces[0]

#  该函数读取所有的训练图像，从每个图像检测人脸并将返回两个大小列表，分别为脸部信息和标签

def prepare_training_data(data_folder_path):
    # 获取文件夹中的目录 （每个主题要有一个目录）
    dirs = os.listdir(data_folder_path)
    # 新建两个列表分别保存所有的脸部和标签
    faces = []
    labels = []

    # 浏览每个目录并访问所有的图像
    for dir_name in dirs:
        label = int(dir_name)
        # 建立包含当前主题图像的文件路径
        subject_dir_path = data_folder_path + "/" + dir_name

        # 获取给定目录内的图像名称
        subject_image_name = os.listdir(subject_dir_path)

        #  浏览每张图片并检测脸部，并将脸部信息保存到列表
        for image_name in subject_image_name:
            # 建立图像路径
            image_path = subject_dir_path + "/" + image_name

            # 读取图片
            image = cv2.imread(image_path)

            # 显示图像0.1s
            cv2.imshow("training on image...", image)
            cv2.waitKey(100)     # ms
            # 检测脸部
            face, rect = detect_face(image)
            # 忽略未检测的脸部
            if face is not None:
                # 将检测的脸部添加到脸部列表中
                faces.append(face)
                labels.append(label)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, labels



# 调用prepare_training_data函数
faces, labels = prepare_training_data("train_data1")

# 创建LBPH识别器并开始训练，也可以使用其他的识别器  Eigen Fisher
face_recongnizer = cv2.face.LBPHFaceRecognizer_create()
face_recongnizer.train(faces, np.array(labels))
face_recongnizer.write('trainer.yml')

