#coding=utf-8

import re
test_str = '''
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
'''
ret = re.search(r'https://.*?\.jpg', test_str)
print(ret)