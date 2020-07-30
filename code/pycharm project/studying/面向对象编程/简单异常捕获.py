#提示用户输入一个整数
#使用8除以用户输入的整数并且输出
try:
    #不能确定正常执行的代码
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数：")
# except ZeroDivisionError:
#     print("除 0 错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    #没有异常才执行
    print("尝试成功")
finally:
    print("无论是否出现错误都会执行的代码")
print("-" * 50)

