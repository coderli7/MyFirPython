from functools import reduce

# 01.map 是指定义一个系统函数，接受一个函数，另外一个参数为一个list,map函数会对list中的
# 每一个元组执行 函数，后返回一个itrable,
# 此功能通过循环也能实现，只不过比较复杂，不够简单明了

# def mi(a):
#     return a**3
# retVal1=map(mi,[1,2,3,4,5])
# print(list(retVal1))


# 02.reduce 是指接受函数和list,list中必须有两个参数，reduce函数，会从list中每次取出两个，然后将结果继续和第三个执行相同操作

# 例1(求和)

# def reducefn1(a,b):
#     return a+b
#
# retval2=reduce(reducefn1,[1,2,3,4])
# print(retval2)
# print(sum([1,2,3,4])) 此处虽然可以使用sum直接求和，但是更复杂的就不能实现了

# 例如下面的list想变成 12345 会更直接
# list1=[1,2,3,5]
#
# def reducefn2(a,b):
#     return a*10+b
#
# print(reduce(reducefn2,list1))




# 03.高级训练,通过mapduce将一个字符串转化为int

str1='1234420KKKK9789'

numDic={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

# intList= map(lambda m1:numDic[m1],str1)

intVal=reduce(lambda r1,r2:r1*10+r2,map(lambda m1:numDic[m1],str1))


print(intVal)
# print(str1+1)







