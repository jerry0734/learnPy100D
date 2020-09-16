"""
读写JSON文件
| JSON                | Python       |
| ------------------- | ------------ |
| object              | dict         |
| array               | list         |
| string              | str          |
| number (int / real) | int / float  |
| true / false        | True / False |
| null                | None         |

| Python                                 | JSON         |
| -------------------------------------- | ------------ |
| dict                                   | object       |
| list, tuple                            | array        |
| str                                    | string       |
| int, float, int- & float-derived Enums | number       |
| True / False                           | true / false |
| None                                   | null         |
"""
import json

filename = 'Day11\\res\\json1.json'
my_dict = {
    'name': 'jerry',
    'age': 3,
    'gender': 'M',
}
mylist = ['123', 456]

print(json.dumps(mylist))

with open(filename, 'w', encoding='utf-8') as json_file:
    json.dump(my_dict, json_file)
    json_file.close()

with open(filename, 'r', encoding='utf-8') as json_read:
    message = json.load(json_read)
    for k,v in message.items():
        print(f'{k} is {v}')
