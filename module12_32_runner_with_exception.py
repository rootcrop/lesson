
class Runner:
    def __init__(self, name, speed=5):
        #self.name = name
        self.distance = 0
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'имя только строка ({type(name).__name__})')

        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'скорость должна быть положительной ({speed})')

    def run(self):
        #self.distance += 10
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

#r=Runner('Vasia', speed=9);      r.run();    print(r.distance)   # 18