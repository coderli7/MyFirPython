import functools

#01.偏函数Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点


# print(int('12345'))
#
# print(int('12345',base=16))
# print(int('7456',16))
#
# print(int('12345',8))
# print(int('12345',8))


def int2(x, base=2):
    return int(x, base)

# print(int2('1000000'))


# 02.functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


int3= functools.partial(int, base=2)
print(int3('1010101'))


max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
# 以上和下面类似相当于
args = (10, 5, 6, 7)
print(max(*args))

