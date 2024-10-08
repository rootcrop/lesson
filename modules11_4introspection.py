from inspect import getmodule   # getmodule     показывает модуль которому принадлежит объект
import pprint as pp

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
    dict['type'] = type(object).__name__
    dict['attributes'] = object.__dict__          # dir(object) вернет методы(это "функции" внутри объекта)
    dict['methods'] = dir(object)
    dict['module'] = getmodule(object).__name__     # выводим имя модуля которому принадлежит объект
    dict['path'] = getmodule(object)                # выводим путь к модулю
    return dict
''' return {
        'type': type(object).__name__,
        'attributes': object.__dict__,          # dir(object) вернет методы(это "функции" внутри объекта)
        'methods': dir(object),
        'module': getmodule(object).__name__,   # выводим имя модуля которому принадлежит объект
        'path': getmodule(object)               # выводим путь к модулю     } '''

class TestClass1:
    def __init__(self,val1):
        self.val1=val1

testObject=TestClass1('q')
number_info = introspection_info(testObject)
pp.pprint(number_info)

#for key, value in number_info.items():
#        print(key, value)
