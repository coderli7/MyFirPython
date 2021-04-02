
# filter 顾名思义，同map类似，也是内置函数，依次将元素作用于函数，根据返回true或false,过滤元素


list1=range(1,101)
list2=list(filter(lambda f1:f1%3==1,list1))
print(list2)

