import sys
import threading
import time
from random import randint

lock = threading.Lock()

class Bank(threading.Thread):

    def __init__(self, balance = 0):
        threading.Thread.__init__(self)
        self.balance = balance

    def deposit(self):
        lock.acquire()
        transaction = 100
        for i in range(1,transaction):
            dep = randint(50,500)
            self.balance = self.balance + dep
            if self.balance >= 500 and lock.locked():
                lock.release()
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            
        time.sleep(0.001)

    def take(self):
        lock.acquire()
        transaction = 100
        for i in range(1, transaction):
            take_ = randint(50,500)
            print(f'Запрос на {take_}')
            if self.balance >= take_:
                self.balance = self.balance - take_
                print(f"Снятие {take_}. Баланс: {self.balance}")
            elif self.balance < take_:
                if lock.locked() == True:
                    print(f"Запрос отклонен, недостаточно средств")
                    break
                print(f"Запрос отклонен, недостаточно средств")
                lock.acquire()
            









bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,), daemon=True)
th2 = threading.Thread(target=Bank.take, args=(bk,),daemon=True)

th1.start()
th2.start()
th1.join()
th2.join()



print(f"Итоговый баланс: {bk.balance}")
