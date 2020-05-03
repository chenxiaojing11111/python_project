'''
********************
Author: cxj
Date: 2020-05-02
********************
'''
'''
break：全部退出
continue：只退出一次
'''
i = 0
while i < 5:
    if i == 3:
        break   # 5后面的数据都不会输出
    print(i)
    i += 1



i = 0
while i < 5:
    i += 1
    if i-1 ==3:
        continue # 除了3都会输出
    print(i-1)


