from PIL import Image

image = Image.open('1.jpg')
# print(image.size)#image.fomat;image.size;image.mode

#裁剪图像
# rect = 125,125,250,250#取图片右下角四分之一
# image.crop(rect).show()

#生成缩略图
# size = 128 , 128#像数变为128*128
# image.thumbnail(size)
# image.show()

#缩放和黏贴图像
# image1 = Image.open('2.png')
# image2 = Image.open('1.jpg')
# rect = 125,125,250,250
# guido_head = image2.crop(rect)
# width, height = guido_head.size
# image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

#旋转和翻转
# image.rotate(-45).show()#正角度表示逆时针旋转，负角度表示顺时针旋转
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

#操作像数
# for x in range(50,150):
#     for y in range(20,120):
#         image.putpixel((x,y),(256,0,0))#对指定区域进行颜色覆盖：红色
# image.show()

#滤镜效果
from PIL import ImageFilter
image.filter(ImageFilter.CONTOUR).show()