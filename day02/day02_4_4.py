'''
********************
Author: cxj
Date: 2020-05-02
********************
'''

str = '1111'
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
for ele in str:
    if ele in container:
        pass
    else:
        print('密码不合法')
        break
else:
    print('密码合法')