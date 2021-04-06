from datetime import *

dtnow=datetime.now()
print(dtnow)
print(type(dtnow))

dt1=datetime(2020,4,6,14,0,22)
print(dt1)

print(datetime.now().timestamp())

print('======================')

#01.字符串转化为datetime

day1 = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(day1)

#02.datetime转化为字符串
day2=datetime.now()
print(day2.strftime('%Y-%m-%d %H:%M:%S'))
print(day2.strftime('%a, %b %d %H:%M'))



dtFormat='%Y-%m-%d %H:%M:%S'
day3=datetime.now()

tmp1=day3 + timedelta(hours=10)
print(tmp1.strftime(dtFormat))

tmp1=day3 + timedelta(days=10)
print(tmp1.strftime(dtFormat))

tmp1=day3 + timedelta(days=365)
print(tmp1.strftime(dtFormat))

tmp1=day3 + timedelta(days=1,hours=1)
print(tmp1.strftime(dtFormat))