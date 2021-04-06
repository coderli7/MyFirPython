# 01.此类型函数，就是将函数内的函数作为一个返回值返回，懒加载

# def fun1(*args):
#     def sum():
#         retVal=0
#         for i in args:
#             retVal=retVal+i
#         return retVal
#     return sum
#
# f1=fun1(1,2,3)
# f2=fun1(1,2,3)
# print(f1)
# print(f2)
# print(f1())
# print(f2())
#
# print(f1==f2)


# 02.重点注意：
#       1.返回的函数并非立即执行，是直到调用后，才执行
#       2.此处注意，返回的3个函数，都是9

def fun2():
    fs=[]
    for i in range(1,4):

        def f():
            return i**2

        fs.append(f)

    return fs

f1,f2,f3=fun2()

print(f1())
print(f2())
print(f3())

# 03.以上，如果必定需要循环引用变量，是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def fun3():

    def f(j):
        def g():
            return j**2

        return g

    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3=fun3()

print(f1())
print(f2())
print(f3())


