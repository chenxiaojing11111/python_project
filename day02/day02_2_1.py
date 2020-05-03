'''
********************
Author: cxj
Date: 2020-05-02
********************
'''
# 循环打印星星
row = 1
while row < 10:
    col = 1
    while col <=row:
        print('*',end='')  # 默认换行
        col += 1
    # 换行
    print()
    row += 1

# 打印九九乘法表
row = 1   # 从1开始
while row < 10:
    col = 1
    while col <= row:
        print('%d * %d = %d' %(col,row,col*row),end='\t')
        col += 1
    # 换行
    print()
    row += 1


#倒序九九乘法表
row = 9
while row > 0:
    col = 1
    while  col <= row:
        print('%d * %d = %d' %(col,row,col*row),end='\t')
        col += 1
    print()
    row -= 1