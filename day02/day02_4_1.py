'''
********************
Author: cxj
Date: 2020-05-02
********************
'''

for ele in range(100,1000):
    hun = ele//100
    ten = ele%100//10
    single = ele%10
    # 判断立方和
    if (hun**3+ten**3+single**3)==ele:
        print(ele)