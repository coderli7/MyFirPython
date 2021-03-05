from collections import deque
# 列表的操作

list1=[1,2,3,4]
list1.append(7)
list1.append(9)
print(list1)

# 列表当做堆栈使用
# print(list1)
# list1.pop()
# print(list1)
# list1.pop()
# print(list1)

# 列表当做队列使用
queue=deque(list1)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

