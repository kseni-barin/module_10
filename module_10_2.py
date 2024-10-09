from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('имя рыцаря должно быть строкой')
        if isinstance(power, int):
            self.power = power
        else:
            raise TypeError('силу рыцаря необходимо вводить числом')

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_enemy = 100
        count_day = 0
        while count_enemy:
            sleep(1)
            count_enemy -=self.power
            count_day+=1
            print(f'{self.name} сражается {count_day} день(дня), осталось воинов {count_enemy}.')
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
