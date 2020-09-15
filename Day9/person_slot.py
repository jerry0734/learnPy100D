class Person():

    # __slots__限定Person类中的属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender


person = Person('锤子', 18, 'M')
print(person.name)
# 限定属性后，score属性不能添加到Person类
# person.score = 100
# print(person.score)
