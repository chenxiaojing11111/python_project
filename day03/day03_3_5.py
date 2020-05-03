'''
author: chenxiaojing
date: 2020-05-03
'''

def calc(a,b):
    '''
    求a+b以及a-b的结果
    :param a:
    :param b:
    :return:
    '''
    sum = a + b
    result = a - b
    return sum,result

sum,result = calc(10,20)
print(sum,result)