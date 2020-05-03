'''
********************
Author: cxj
Date: 2020-05-02
********************
'''

# 循环结合else
# 格式：
'''
for 变量 in 容器:
    循环体代码
else:
没有通过break退出循环，循环结束后，会执行的代码
'''
str = 'hello world'
for ele in str:
    print(ele)
else:
    print('执行了else语句')

# for else中执行了continue
for ele in str:
    if ele == 'l':
        continue
    print(ele)
else:
    print('执行了else语句')

# for else中执行了break
for ele in str:
    if ele == '1':
        break
    print(ele)
else:
    print('执行了else语句')