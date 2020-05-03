'''
author: chenxiaojing
date: 2020-05-03
'''

# 函数的四种类型
# 无参无返回值函数
def sayHello():
    print('hello')

sayHello()

# 无参有返回值函数
import random
def getTemp():
    return random.randint(0,100)

a = getTemp()
print(a)

# 有参无返回值函数
def sayHello1(name):
    print('hello %s' %name)

sayHello1('chenxiaojing')

# 有参有返回值函数
def sum(a,b):
    return a+b

# a = sum(1,2)
# print(a)
print(sum(1,2))

def func1():
    b = 20
    print('hello%d' %b)

func1()

# 全局变量
m = 10
n =20
def func():
    print(m)

func()

# 函数内部修改全部变量
m = 10
def func():
    global m
    m = 30
    print(m)

func()




