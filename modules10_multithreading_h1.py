import time
from threading import Thread
#from datetime import datetime

''' Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
    10, example1.txt
    30, example2.txt
    200, example3.txt
    100, example4.txt

После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
    10, example5.txt
    30, example6.txt
    200, example7.txt
    100, example8.txt

Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию. '''
#
ts=time.time() #datetime_start=datetime.now()

# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество
# записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в
# соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1,word_count+1):
            f.write(f'какое-то слово N {i} \n'); time.sleep(0.1)
    print(f'завершилась запись в файл {file_name}')

write_words(10, 'modules10_multithreading_example1.txt')
write_words(30, 'modules10_multithreading_example2.txt')
write_words(200, 'modules10_multithreading_example3.txt')
write_words(100, 'modules10_multithreading_example4.txt')
print (f'работа функции : {time.time()-ts:.3f}')  # print (f'прошло времени: {datetime.now()-datetime_start}')

ts=time.time()
thread1=Thread(target=write_words, args=(10, 'modules10_multithreading_example5.txt'))   # инициализируем потоки
thread2=Thread(target=write_words, args=(30, 'modules10_multithreading_example6.txt'))
thread3=Thread(target=write_words, args=(200, 'modules10_multithreading_example7.txt'))
thread4=Thread(target=write_words, args=(100, 'modules10_multithreading_example8.txt'))

thread1.start() # запускаем потоки
thread2.start(); thread3.start(); thread4.start()

thread1.join()  # ловим окончание иполнения потока
thread2.join(); thread3.join(); thread4.join()

print (f'работа потока : {time.time()-ts:.3f}')