
''' Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
    test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
Пункты задачи:
    Скачайте исходный код для тестов.
    Создайте класс RunnerTest и соответствующие описанию методы.
    Запустите RunnerTest и убедитесь в правильности результатов.

Пример результата выполнения программы:
Вывод на консоль:
Ran 3 tests in 0.001s OK

Примечания:
    Попробуйте поменять значения в одном из тестов, результаты  '''

import unittest, module12_2_runner as runner
# r=rn.Runner('Vasia')    # r.run(); r.walk()   # print(r, r.distance)   # Vasia 15     # print(type(r.run)) # <class 'method'>

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rw=runner.Runner('Vasia')
        for _ in range(10):
            rw.walk()
        self.assertEqual(rw.distance, 50, f' runner {rw} distance: {rw.distance}, target walk: 50')

    def test_run(self):
        rr = runner.Runner('Pasha')
        for _ in range(10):
            rr.run()
        self.assertEqual(rr.distance, 100, f' runner {rr} distance: {rr.distance}, target run: 100')

    def test_challenge (self):
        rw = runner.Runner('Vasia')
        rr = runner.Runner('Pasha')
        for _ in range(10):
            rw.walk()
            rr.run()
        self.assertNotEqual(rr.distance, rw.distance, f' runner1 distance: {rr.distance}, runner2 distance: {rw.distance},')

#r=RunnerTest()
#print(r.test_walk())
#print(r.test_run())
#print(r.test_challenge())
