'''
author: chenxiaojing
date: 2020-05-03
'''


t = ('林青霞','张曼玉','王祖贤')
name1,name2,name3 = t
print(name1,name2,name3)

# 常规交换
a = 10
b = 20
tmp = a
a = b
b = tmp
print(a,b)


# 元组交换
a = 10
b = 20
a,b = b,a
print(a,b)

# 列表不可修改
l = [10,20,30]
t = tuple(l)
print(t)

#函数
def sayHello():
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')

# 3 调用函数
sayHello()