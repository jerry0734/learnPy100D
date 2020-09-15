"""@property装饰器"""


class Person():

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    # getter 获取某个值
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter 设定修改某个值
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print(f'{self._name} is playing chess.')
        else:
            print(f'{self._name} is playing poker.')


person = Person('jerry', 3)
print(person.age)
person.play()
person.age = 16
person.play()
