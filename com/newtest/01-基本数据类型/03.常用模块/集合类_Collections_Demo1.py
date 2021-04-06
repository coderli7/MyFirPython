
from collections import *
from urllib import request,parse

# 解析xml
from xml.parsers.expat import ParserCreate
# 解析html
from html.parser import HTMLParser
from html.entities import name2codepoint



# 01.namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
Point =namedtuple('Point',['a','b'])
p1=Point(2,3)
print(p1.a)
print(p1.b)

print(isinstance(p1,Point))
print(isinstance(p1,tuple))

# 同理，可以用来表示一个圆形

Circle = namedtuple('Circle', ['x', 'y', 'r'])


# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：


q = deque(['a', 'b', 'c'])

q.appendleft('0')
print(q)


dict1 = defaultdict(lambda: 'N/A')
print(dict1['dd'])


dict2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# Counter是一个简单的计数器，例如，统计字符出现的个数：







with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


