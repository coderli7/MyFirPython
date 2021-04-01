
import  os

from collections.abc import *

# 01.快速生成列表

# print(list(range(1,101)))


# list1=[]
# for i in range(1,101):
#     list1.append(i**3)
# print(list1)

# 可以更直接简化
# print([x**3 for x in range(1,101)])


# 循环列出当前目录


# print([dir for dir in os.listdir('.')])


# 02.如果自动推导出的列表中包含数据量巨大，则比较占内存，



# 以上使用中括号的是一个列表，会把结果生成到内存中去，
# 以下，圆括号，保存的是算法,同时也是一个迭代器

gen1= (y**2 for y in range(1,11))
print(gen1)
print(isinstance(gen1,Iterable))
print(next(gen1))
print("**************")
print(next(gen1))
print("**************11")

for i in gen1:
    print(i)

