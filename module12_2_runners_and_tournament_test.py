from module12_2_runners_and_tournament import Runner, Tournament
from unittest import TestCase

class TournamentTest(TestCase):
    def setUp (self):
        self.runner1=Runner ('Усэйн',10)
        self.runner2=Runner ('Андрей',9)
        self.runner3=Runner ('Ник',3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}    # dict

    def test_tournament_1 (self):
        tournament=Tournament(90, self.runner1, self.runner3)
        result=tournament.start()
        TournamentTest.all_results['1']=result  #
        self.assertTrue(result[1]=='Усэйн')

    def test_tournament_2 (self):
        tournament=Tournament(90, self.runner2, self.runner3)
        result=tournament.start()
        TournamentTest.all_results['2']=result
        self.assertTrue(result[1]=='Андрей')

    def test_tournament_3 (self):
        tournament=Tournament(90, self.runner1, self.runner2, self.runner3)
        result=tournament.start()
        TournamentTest.all_results['3']=result
        self.assertTrue(result[1]=='Усэйн')

    @classmethod
    def tearDownClass (cls):
        for key, value in cls.all_results.items():
            print(f'1: {value[1]}, 2: {value[2]}')
