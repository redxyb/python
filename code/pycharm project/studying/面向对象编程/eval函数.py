# #基本的数学计算
# print(eval("1+1"))#2
# #字符串重复
# print(eval("'*' * 10"))#**********
# #将字符串转换为列表
# print(type(eval("[1,2,3,4,5]")))#<class 'list'>
# #将字符串转换为字典
# print(type(eval("{'name':'xiaoyuebin','age':22}")))#<class 'dict'>

#需求：1.提示用户输入一个加减乘除混合运算；2.返回计算结果
input_str = input("请输入一个算数题：")
print(eval(input_str))