'''Задача "План перехват": Напишите 2 функции:
Функция personal_sum(numbers):
    Должна принимать коллекцию numbers.
    Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
    В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.

Функция calculate_average(numbers)
Среднее арифметическое - сумма всех данных делённая на их количество.
    Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
    Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
    Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None. '''

def personal_sum(numbers):
    result=0; incorrect_data=0
    try:
        for n in numbers:
            try:
                result+=n              # суммируем в result
            except TypeError:          # обработка ошибки int+string
                print(f"в numbers записан некорректный тип данных - {n}")
                incorrect_data+=1
    except TypeError:
        print ('В numbers записан некорректный тип данных')     # одно число не итерабельно
        return None
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result2=personal_sum(numbers)
        summ=result2[0]
        incorrect_data=result2[1]
    except:
        return None
    try:
        result= summ/(len(numbers)-incorrect_data)
    except ZeroDivisionError:       # обработка ошибки /0
        result=0
    return result

#print(f'Результат 1: {calculate_average("1, 2, 3")}')
#print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
#print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
#print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
