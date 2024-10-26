from inspect import getmodule   # getmodule     показывает модуль которому принадлежит объект
import pprint as pp
from itertools import count

''' Задание: Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип'''

def introspection_info(object):
    dict={}
    method_arr=[]   #
    dict['type'] = type(object).__name__
    dict['attributes'] = object.__dict__
    #dict['methods'] = dir(object)                # dir(object) вернет список атрибутов и методов (это "функции" внутри объекта) а нужно только методы, проверяем через callable()
    for obj in dir(object):
        if callable(getattr(object, obj)):
            method_arr.append(obj)
    dict['methods']=dir(zip(method_arr))
    dict['module'] = getmodule(object).__name__     # выводим имя модуля которому принадлежит объект
    dict['path'] = getmodule(object)                # выводим путь к модулю
    return dict


class TestClass1:                               # just example
    def __init__(self,val1):
        self.val1=val1

testObject=TestClass1('q')

number_info = introspection_info(testObject)
pp.pprint(number_info)

#for key, value in number_info.items():
#        print(key, value)

# 1. Методы возвращаются неверно - dir() возвращает список атрибутов и методов. Из этого списка нужно отобрать методы.
# Можно сделать это с помощью функции callable, проходясь по каждому элементу списка и проверяя вызываемый ли он.
# Точно также можно отобрать атрибуты, не прибегая к obj.__dict__
# 2. Вместо getmodule(obj) можно использовать obj.__class__.__module__