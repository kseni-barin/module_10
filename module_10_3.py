from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            add_balance = randint(50, 500)
            self.balance = self.balance + add_balance
            print(f'Пополнение: {add_balance}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            subtract_balance = randint(50, 500)
            print(f'Запрос на {subtract_balance}')
            if subtract_balance <= self.balance:
                self.balance = self.balance - subtract_balance
                print(f'Снятие: {subtract_balance}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
