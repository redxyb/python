def is_palindrome(n):#筛选函数：从左向右读和从右向左读都是一样的
    s = str(n)
    s1 = s[::-1]
    if s1 == s:
        return True
    else:
        return False
output = filter(is_palindrome,range(1,100))
print('1-100:',list(output))