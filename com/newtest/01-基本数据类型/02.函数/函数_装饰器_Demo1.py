import functools


# 01.函数也是对象
# def fun1():
#     return 1
#
# f1=fun1()
# print(f1)
# print(fun1.__name__)

# 02.如要实现函数前后打印日志的功能，则需要装饰器

def fun2_log(fun):
    def wrapper(*args,**kw):
        print('call %s():'%fun.__name__)
        return fun(*args,**kw)
    return wrapper

def fun2_log1(text):
    def decorator(fun):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,fun.__name__))
            return fun(*args,**kw)
        return wrapper
    return decorator

def fun2_log2(text):
    def decorator(fun):
        @functools.wraps(fun)#主要为解决函数名称问题
        def wrapper(*args,**kw):
            print('%s %s():'%(text,fun.__name__))
            return fun(*args,**kw)
        return wrapper
    return decorator


@fun2_log
def fun3_name(name):
    print('hello!',name)

# fun3_name('lucy')


@fun2_log1('excute')
def fun3_name1(name):
    print('hello!',name)

fun3_name1('lucy')

print(fun3_name1.__name__)

print('=========================')

@fun2_log2('excute2')
def fun3_name2(name):
    print('hello!',name)

fun3_name2('lucy')

print(fun3_name2.__name__)

