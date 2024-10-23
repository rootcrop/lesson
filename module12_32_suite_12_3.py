import unittest
import module12_31_runner_test
import module12_31_runners_and_tournament_test

# Задача "Заморозка кейсов"                         

''' Часть 1. TestSuit.
    Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
    Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
    Создайте объект класса TextTestRunner, с аргументом verbosity=2. '''

runner_testSuite= unittest.TestSuite()
runner_testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module12_31_runner_test.RunnerTest))
runner_testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module12_31_runners_and_tournament_test.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_testSuite)

''' Часть 2. Пропуск тестов.
    Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
    Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase. '''