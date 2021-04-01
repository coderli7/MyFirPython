# 只要是可迭代对象，均可迭代，字典也可迭代

from collections.abc import Iterable, Iterator


# dic1={'a':'1','b':'2','c':'3'}
# for item in dic1:
#     print(dic1[item])
#

# 01.如何判断对象是否可迭代呢，使用collections中的Itrable
#
# b1=isinstance('abx',Iterable)
# print(b1)
#
# print(isinstance(123,Iterable))

# 02.如果在Python中，想通过类似java中下标的方式访问元素，可以使用自带函数转义

#
# list1=['A','N',"C"]
# for idx,value in enumerate(list1):
#     print(idx,value)

# 03.直接通过 两个元素访问数据,比较常见
# list2=[(1,'A'),(2,'B'),(3,'C')]
# for x,y in list2:
#     print(x,y)





