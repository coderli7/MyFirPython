# 元组初始化，可以没有括号
# tuple1=1,2,3,4
#
#
# print(tuple1)
#
# tuple2=tuple1,('2','a')
# print(tuple2)
# print(tuple2[0])
# print(tuple2[1])
# print(tuple2[2])

# 获取到索引
# for x,y in enumerate(['a','b','c']):
#     print(x,y)

# 使用zip遍历多个组合

questions=['name','age','gender']
answer=['bruce','31','男']

for q,s in zip(questions,answer):
    print('\nwhat is your {0} ? \n  *************》》》 \nIt is \"{1}\"\n '.format(q,s))