class Runner:
    def __init__(self, name, speed=5):      # атрибут speed для определения скорости бегуна
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2     #  изменение дистанции зависит от скорости

    def walk(self):
        self.distance += self.speed         #  изменение дистанции зависит от скорости

    def __str__(self):
        return self.name

    def __eq__(self, other):                # Метод __eq__ для сравнивания имён бегунов
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:       #  класс соревнований, где есть вся дистанция и список участников
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):    #  метод start, реализует логику бега по предложенной дистанции
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers
