# python json 序列化
import json

t = dict(name='zsw', age='18', score='100')  # dict() 字典
dumps = json.dumps(t)
print(dumps)  # dumps()方法返回一个str，内容就是标准的JSON。

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
loads = json.loads(json_str)
print(loads)  #JSON反序列化为Python对象


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def to_dict(self):
        return {'name': self.name, 'age': self.age}

def decode_person(dct):
    if 'name' in dct and 'age' in dct:
        return Person.from_json(dct)
    return dct

def encode_person(obj):
    if isinstance(obj, Person):
        return obj.to_dict()
    return json.JSONEncoder.default(obj)


json_str = '{"name": "Charlie", "age": 35}'
person = json.loads(json_str, object_hook=decode_person)
print(f"Name: {person.name}, Age: {person.age}")  # 输出: Name: Charlie, Age: 35

person = Person("Alice", 30)
json_str = json.dumps(person, default=encode_person)
print(json_str)  # 输出: {"name": "Alice", "age": 30}

