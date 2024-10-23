import unittest, module12_31_runner as runner

class RunnerTest(unittest.TestCase):
    is_frozen=False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rw=runner.Runner('Vasia')
        for _ in range(10):
            rw.walk()
        self.assertEqual(rw.distance, 50, f' runner {rw} distance: {rw.distance}, target walk: 50')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rr = runner.Runner('Pasha')
        for _ in range(10):
            rr.run()
        self.assertEqual(rr.distance, 100, f' runner {rr} distance: {rr.distance}, target run: 100')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge (self):
        rw = runner.Runner('Vasia')
        rr = runner.Runner('Pasha')
        for _ in range(10):
            rw.walk()
            rr.run()
        self.assertNotEqual(rr.distance, rw.distance, f' runner1 distance: {rr.distance}, runner2 distance: {rw.distance},')

#r=RunnerTest()         #print(r.test_walk())
#print(r.test_run())    #print(r.test_challenge())
