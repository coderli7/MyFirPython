import  keyword as kw

# print(kw.kwlist)


class Person:

    name = ''
    age = ''

    def __init__(self):
        self.name='张三'
        self.age='10'

    def __init__ (self,nameParam,ageParam):
        self.name=nameParam
        self.age=ageParam

    def speak(self):
        return "姓名是:"+self.name+";"+"年龄是:"+self.age


if __name__ == '__main__':

    # p1 = Person()
    # p1.age='18'
    # p1.name='bruce'
    # print(p1.speak())
    p2 = Person('李四','21')
    print(p2.speak())

    p3 = Person('赵四', '56')
    print(p3.speak())










