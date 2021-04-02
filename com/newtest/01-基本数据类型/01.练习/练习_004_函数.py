
# 01.函数可以当做变量名使用
# def myAddfun(a,b):
#     return a+b
#
# f1=myAddfun
# ret1=f1(1,2)
# print(ret1)


# 02.匿名函数

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

f2=lambda x1:x1+1
for i in range(11):
    print(f2(i))




