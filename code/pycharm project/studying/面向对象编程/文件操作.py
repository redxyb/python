#1.打开文件
file = open("test", "r")
file2 = open("test[附件]", "a")
#a:追加写入   w:覆盖写入

#2.读取文件内容
# # text = file.read()
# while True:
#     text = file.readline()#读取完一行，文件指针移动到下一行
#     if not text:#判断是否读取到文件
#         break
#     print(text)
# print(len(text))

#复制文件
while True:
    text = file.readline()
    if not text:
        break
    file2.write(text)

#写入文件
# file.write("xiaoyuebin")

#3.关闭文件
file.close()
file2.close()