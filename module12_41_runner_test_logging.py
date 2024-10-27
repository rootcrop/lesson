import unittest, module12_32_runner_with_exception as runner
from unittest import TestCase
import logging

# или отсюда запускать лог или из setUpClass(cls)
# logging.basicConfig(level=logging.INFO, filemode='w', filename='module12_41_runner_test_logging.log', encoding='utf-8', format='%(asctime)s // %(levelname)s // %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen=False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='module12_41_runner_test_logging.log', encoding='utf-8', format='%(asctime)s // %(levelname)s // %(message)s')

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rw=runner.Runner('Vasia')
            for _ in range(10):
                rw.walk()
            self.assertEqual(rw.distance, 50, f' runner {rw} distance: {rw.distance}, target walk: 50')
            logging.info('test_walk выполнен успешно')
        except ValueError as error:
            logging.warning('Неверная скорость для Runner', exc_info=error)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rr = runner.Runner('Pasha')
            for _ in range(10):
                rr.run()
            self.assertEqual(rr.distance, 100, f' runner {rr} distance: {rr.distance}, target run: 100')
            logging.info('test_run выполнен успешно')
        except TypeError as error:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=error)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge (self):
        rw = runner.Runner('Vasia')
        rr = runner.Runner('Pasha')
        for _ in range(10):
            rw.walk()
            rr.run()
        self.assertNotEqual(rr.distance, rw.distance, f' runner1 distance: {rr.distance}, runner2 distance: {rw.distance},')

if __name__=='__main__':
    unittest.main()
