'''
********************
Author: cxj
Date: 2020-05-02
********************
'''

# if...elif...else
'''
需求：
1. 定义 holiday_name 字符串变量记录节日名称
2. 如果是 情人节 应该 买玫瑰／看电影
3. 如果是 平安夜 应该 买苹果／吃大餐
4. 如果是 生日 应该 买蛋糕
5. 其他的日子每天都是节日啊……
'''
holiday_name = input('请输入节目名称')
if holiday_name=='情人节':
    print('买玫瑰/看电影')
elif holiday_name=='平安夜':
    print('买苹果/吃大餐')
elif holiday_name=='生日':
    print('买蛋糕')
else:
    print('每天都是节日，每天一个红包')
