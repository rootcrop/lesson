''' Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
    Атрибут объекта model - название автомобиля (строка).
    Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
    Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Атрибут __numbers - номера автомобиля (строка).
    Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
    Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
    Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
    Возвращает True, если исключения не были выброшены.

__is_valid_numbers
    Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
    Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
    Возвращает True, если исключения не были выброшены. '''

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message=message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message=message

class Car:
    def __init__(self, model, vin, number):
        self.model=model
        #self.__vin=self.__is_valid_vin(vin)    # true
        if self.__is_valid_vin(vin):            # true
            self.__vin=vin
        #self.__number=self.__is_valid_number(number)
        if self.__is_valid_number(number):      # true
            self.__number=number

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber ('некоректный тип vin номера: '+vin)
        if vin < 1_000_000 or vin > 9_999_999:  #if vin not in range (1_000_000, 10_000_000):
            raise IncorrectVinNumber ('неверный диапазон для vin номера: '+vin)
        return True

    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers ('некорретный тип данных для номеров : '+number)
        if len(number)!=6:
            raise IncorrectCarNumbers("неверная длина номера : "+number)
        return True

    def is_valid_vin(self):
        print(self.vin)
        pass

    def is_valid_numbers(self):
        print(self.number)
        pass

try:
  first = Car('Model1', 1_000_000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

'''
try:
  second = Car('Model2', 3000000, 'т1001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
'''