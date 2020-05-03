'''
********************
Author: cxj
Date: 2020-05-02
********************
'''

'''
需求：打印棱形
*****
****
***
**
*
'''

''''
row = int(input("请输入打印的行数:"))
n = row
while n >= 0:
    X = "*" * n
    print(X)
    n -= 1   # n=n-1
'''
row = int(input("请输入行数:"))
n = row
while n>0:
    x="*" * n
    y=" " *(row-n)
    print(y+x)
    n -=1

'''
n = int(input("Enter the number of rows:"))
i = 1
while i<=n:
    print("*" * i)
    i += 1
'''
'''
n = int(input('请输入行数:'))
i = 1
while i<= n:
    print("*" * i)
    i += 1
'''

