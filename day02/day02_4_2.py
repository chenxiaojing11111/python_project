'''
********************
Author: cxj
Date: 2020-05-03
********************
'''

# 数字组合
for hun in range(1,5):
    for ten in range(1,5):
        for single in range(1,5):
            if(hun!=ten) and (ten!=single) and (single!=hun):
                num=hun*100+ten*10+single
                print(num)