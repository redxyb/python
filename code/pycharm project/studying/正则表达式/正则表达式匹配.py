import re

while True:
    test_str = input('请输入你要匹配的字符串：')
    regular_expression = input('请输入你匹配字符串的正则表达式：')
    try:
        m = re.match(regular_expression,test_str)
        if m:
            print('ok')
        else:
            print('failed')
    except 0xff == ord('q'):
        break
    finally:
        print(m.groups())#取出要匹配字符串的子串，前提是正则表达式要定义组
