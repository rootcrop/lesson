# Модуль №10. Мультипоточность      
# Практика, часть 2
import requests, pprint, queue, time; from threading import Thread

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'  # codepen.io/bobhami/pen/gwrJNp
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/generator/v1/genre'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

time_start=time.time()
all_songs_url=[]                    # сюда складываем результаты url
all_genre=[]                        # сюда складываем случайные жанры

class GetGenre(Thread):
    def __init__(self, queue):  # первичная инициализация
        self.queue = queue
        super().__init__()      # не забываем проинициализировать родительского класса через super, иначе thread не будет работать
    def run(self):              # авто_старт, пока однопоточная реализация
        response = requests.get(RANDOM_GENRE_API_URL)   # обращаемся по url и берем с binaryjazz случайный жанр
        genre = response.json()
        all_genre.append(genre)
        self.queue.put(genre)                           # кладем в очередь(queue) жанр

class Genius(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()  # не забываем проинициализировать родительского класса через super, иначе thread не будет работать
    def run(self):
        genre = self.queue.get()    # берем из очереди жанр (genre)
        data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})  # обращаемя к GENIUS_API с подготовленным genre
        data = data.json()
        try:                        # обрабатываем ошибки
            song_id = data['response']['hits'][2]['result']['api_path']
            #print(f'{GENIUS_URL}{song_id}/apple_music_player')
            all_songs_url.append(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError as e:
            pass

# один поток
queue = queue.Queue()               # создаем инстанс(сущность) из модуля queue(очередь)
get_genre_thread = GetGenre(queue)  # создаем сущность своего класса GetGenre(получить случ. жанр) и засылаем внутрь ссылку на объект очередь
genius_thread = Genius(queue)

get_genre_thread.start(); genius_thread.start()     # запускаем треды
get_genre_thread.join(); genius_thread.join()       # ловим результаты тредов '''

# ошибка в all_genre 
pprint.pprint(all_genre)        # {'code': 'rest_no_route', 'data': {'status': 404}, 'message': 'No route was found matching the URL and request method.'}
pprint.pprint(all_songs_url)    # https://genius.com/songs/3018471/apple_music_player
