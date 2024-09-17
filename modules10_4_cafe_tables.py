''' Задача "Потоки гостей в кафе": Необходимо имитировать ситуацию с посещением гостями кафе.
Создайте 3 класса: Table, Guest и Cafe, на основе которых имитируется работа кафе:
    Table - стол, хранит информацию о находящемся за ним гостем (Guest).
    Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
    Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).

Примечания:
    Для проверки значения на None используйте оператор is (table.guest is None).
    Для добавления в очередь используйте метод put, для взятия - get.
    Для проверки пустоты очереди используйте метод empty.
    Для проверки выполнения потока в текущий момент используйте метод is_alive. '''

import random, time, threading  #, queue
from queue import Queue

''' Класс Table: Объекты этого класса должны создаваться следующим способом - Table(1)
Обладать атрибутами number - номер стола и guest - гость, 
который сидит за этим столом (по умолчанию None) '''
class Table():
    def __init__(self, number):
        self.number=number
        self.guest=None

''' Класс Guest:
    Должен наследоваться от класса Thread (быть потоком).
    Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    Обладать атрибутом name - имя гостя.
    Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд. '''
class Guest(threading.Thread):      # наследуемся от треда
    def __init__(self, name):
        super().__init__()          # для наследования
        self.name=name
    def run(self):
        time.sleep(random.randint(3,10))

'''Класс Cafe:
    Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция)
    Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей)

Метод guest_arrival(self, *guests):
    Должен принимать неограниченное кол-во гостей (объектов класса Guest).
    Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
    Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".

Метод discuss_guests(self):
Этот метод имитирует процесс обслуживания гостей.
    Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
    Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
    Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
    Далее запустить поток этого гостя (start) '''
class Cafe():
    def __init__(self, queue, *tables): # неограниченное кол-во столов
        self.tables=tables              # <class 'tuple'>
        self.queue = Queue()

    def guest_arrival(self, *guests):       # прибытие неограниченного кол-ва гостей
        for guest in guests:                # перебираем список всех гостей     #if any(table.guest is None for table in self.tables):
            for table in self.tables:       # перебираем столы из списка столов
                if table.guest is None:     # если столик пуст, то можно посадить туда гостя
                    guest.start()           # запускам поток
                    table.guest = guest     # и за стол сажаем гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:                           # если нет мест
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):               # обслуживаем гостей
        while not self.queue.empty() or any([table.guest for table in self.tables]): # пока очередь не пустая или за столом есть хотя бы 1 гость
            for table in self.tables:        # перебираем столы из списка столов
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    table.guest=None
                    print(f"Стол номер {table.number} свободен")
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()      # запускаем поток

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [ 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
