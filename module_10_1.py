from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

data_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

data_end1 = datetime.now()
data_func = data_end1 - data_start
print(f'Работа функции {data_func}')

data_start2 = datetime.now()
thr_five = Thread(target = write_words, args = (10, 'example5.txt'))
thr_six = Thread(target = write_words, args = (30, 'example6.txt'))
thr_seven = Thread(target = write_words, args = (200, 'example7.txt'))
thr_eight = Thread(target = write_words, args = (100, 'example8.txt'))

thr_five.start()
thr_six.start()
thr_seven.start()
thr_eight.start()

thr_five.join()
thr_six.join()
thr_seven.join()
thr_eight.join()
data_end2 = datetime.now()
data_thr = data_end2 - data_start2
print(f'Работа потоков {data_thr}')

