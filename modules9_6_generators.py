''' Задача: Напишите функцию-генератор all_variants(text),
которая принимает строку text и возвращает объект-генератор, 
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
Пункты задачи:
    Напишите функцию-генератор all_variants(text).
    Опишите логику работы внутри функции all_variants.
    Вызовите функцию all_variants и выполните итерации.

Пример результата выполнения программы: Пример работы функции:
a = all_variants("abc")
for i in a: print(i)
Вывод на консоль:
a
b
c
ab
bc
abc '''

#
# itertools             # docs.python.org/3/library/itertools.html
# import itertools      # combinatoric iterators
# itertools.permutations('text', 2))
def all_variants(text):
    for size in range(len(text)):
        for i in range (len(text) - size ):
            print(i, size+i+1)
            yield text[i:size+i+1]

#for i in all_variants('abc'): print(i)
print(list(all_variants('abc')))



