#Задача "Потоки гостей в кафе"
from threading import Thread, Lock
from random import randint
from time import sleep
import queue

class Table:
    def __init__(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            raise TypeError('необходимо передать целое число')
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('имя гостя должно быть строкой')

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        if all(isinstance(element, Table) for element in args):
            self.tables = list(args)
        else:
            raise TypeError('передайте объекты класса Table')
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        if all(isinstance(guest, Guest) for guest in guests):
            list_guests = list(guests)
        else:
            raise TypeError('передайте объекты класса Guest')
        for guest_current in list(guests):
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest_current
                    table.guest.start()
                    print(f'{guest_current.name} сел(-а) за стол номер {table.number}')
                    list_guests.remove(guest_current)
                    break
        if list_guests:
            for element in list_guests:
                self.queue.put(element)
                print(f'{element.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
        if self.queue.empty() and all(table.guest is None for table in self.tables):
            print("Обслуживание завершилось, все гости ушли и все столы свободны.")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for guest in guests:
   guest.join()

