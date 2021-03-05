print("*****************************")
list1=[1,2,3,4,5]
list2=[2,3]
print(list1)
print(list2)
print("*****************************")

# newList1=[4*x for x in list1]
# print(newList1)

# newList2=[[x,x**2] for x in list1]
# print(newList2)

# 新增条件
# newList3=[[x,x**2] for x in list1 if x>2]
# print(newList3)

# newList4=[x*y for x in list1 for y in list2]
# print(newList4)


# newList5=[list1[i]*list2[i] for i in range(len(list2))]
# print(newList5)

# for i in range(5,10):
#     print(i)

# newList6=[str(round(355/113,i)) for i in range(0,10)]
# print(newList6)


matrix = [  [1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# for row in matrix:
#     print(row)

newMatrix=[[row[i] for row in matrix] for i in range(4)]
print(newMatrix)




