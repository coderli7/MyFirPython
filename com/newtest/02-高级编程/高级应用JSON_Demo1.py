import json

data = {'name': 'bruce', 'age': 20}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)


jsonData1=json.loads(json_str)

print('name:'+jsonData1['name'])
print('age:'+str(jsonData1['age']))