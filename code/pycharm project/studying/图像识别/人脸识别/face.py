import cv2
import os
import numpy as np

#  检测人脸

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
faces, labels = prepare_training_data("train_data")

# 创建LBPH识别器并开始训练，也可以使用其他的识别器  Eigen Fisher
face_recongnizer = cv2.face.LBPHFaceRecognizer_create()
face_recongnizer.train(faces, np.array(labels))

#根据给定的（x,y)坐标和宽度高度在图像上绘制矩形
def draw_rectangle(img,rect):
     (x, y, w, h) = rect
     cv2.rectangle(img, (x, y), (x+w, y+h), (128, 128, 0), 2)

# 根据给定的（x,y)坐标标识出人名
def draw_text(img, text, x, y):
     cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 0), 2)


#  建立标签与人名的映射列表
subject =["liudehua", "zhangxueyou"]


# 预测 此函数识别传递的图像中的人物并在检测到的脸部周围绘制一个矩形框及名称
def predict(test_img):
    # 生成图像的副本, 这样是为保留原来的图像
    img = test_img.copy()

    # 检测人脸
    face, rect = detect_face(img)

    # 预测人脸
    #cv2.imshow("face", face)
    label = face_recongnizer.predict(face)

    # 获取由人脸识别器返回的相应标签的名称
    label_text = subject[label[0]]

    # 在检测到的脸部周围画一个矩形
    draw_rectangle(img, rect)    #rect 坐标

    # 标出预测的名字
    draw_text(img, label_text, rect[1], rect[1]-5)

    # 返回检测的图像
    return img

# 加载测试图像
test_img1 = cv2.imread("liudehua.jpg")
test_img2 = cv2.imread("zhangxueyou00.jpg")

#  执行预测
predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)

# 显示两个图像
cv2.imshow(subject[1], predicted_img1)
cv2.imshow(subject[0], predicted_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()