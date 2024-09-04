''' Задание: Напишите 2 функции:
    Функция, которая складывает 3 числа (sum_three)
    Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

Пример: result = sum_three(2, 3, 6); print(result)
Результат консоли:
Простое
11               '''

def is_prime_old(number):       # обычное решение
    divisions_number = 0
    for i in range(1,number+1):
        if number % i == 0: divisions_number += 1
    if divisions_number > 2: res='Простое'
    else: res='Составное'
    return res

def is_prime(func):
    def wrapper(*args):
        result= func(*args)
        divisions_number = 0
        for i in range(1,result+1):
            if result % i == 0: divisions_number += 1
        if divisions_number > 2: print('Составное')
        else: print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6); print(result)


