from operator import itemgetter

# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
#
# print(sorted([36, 5, -12, 9, -21], key=abs))
# print(sorted([36, 5, -12, 9, -21]))
#
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#

# def by_name(t):
#     pass


dic1={'Bob': 75, 'Adam':92, 'Boa':66, 'Lisa':88}


list1=sorted(dic1.items(),key=lambda x:x[0],reverse=False)
list2=sorted(dic1.items(),key=lambda x:x[0],reverse=True)


list3=sorted(dic1.items(),key= itemgetter(0),reverse=False)
list4=sorted(dic1.items(),key= itemgetter(0),reverse=True)

list5=sorted(dic1.items(),key= itemgetter(1),reverse=False)
list6=sorted(dic1.items(),key= itemgetter(1),reverse=True)

# print(list1)
# print(list2)
# print(list3)
# print(list4)
print(list5)
print(list6)

# print(list1==list3)
# print(list2==list4)


# L2 = sorted(L, key=by_name)
# print(L2)
