'''
********************
Author: cxj
Date: 2020-05-02
********************
'''

# 遍历列表
nameList = ['李清霞','张曼玉','胡慧中']
for name in nameList:
    print(name)

# 增加元素
nameList = ['李清霞','张曼玉','胡慧中']
nameList.append('陈晓静')
print(nameList)

# 删除元素
nameList = ['李清霞','张曼玉','胡慧中']
nameList.remove('张曼玉')
print(nameList)

# 修改元素
nameList = ['李清霞','张曼玉','胡慧中']
nameList[1]='陈晓静'
print(nameList)

# 查询
nameList = ['李清霞','张曼玉','胡慧中']
ele = nameList[1]
print(ele)

nameList = ['李清霞','张曼玉','胡慧中']
index = nameList.index('张曼玉')
print(index)

# 列表排序
ageList = [90,40,50,60,70]
ageList.sort()
print(ageList)

# 降序排序
ageList = [90,40,50,60,70]
ageList.sort(reverse=True)
print(ageList)

# 反转

ageList = [90,40,50,60,70]
ageList.reverse()
print(ageList)

# 列表嵌套
students = [['李清霞','张曼玉','胡慧中'],['大乔','小乔','后裔']]
print(students[2])