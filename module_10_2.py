import time
import threading

class Knight(threading.Thread):
    def __init__(self, name,power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        enemies = 100
        days_counter = 1
        print(f"{self.name}, на нас напали")
        while enemies > 0:

            time.sleep(1)
            print(f"{self.name}, сражается {days_counter} день(дня), осталось {enemies - self.power}")
            days_counter += 1
            enemies = enemies - self.power
            if enemies <= 0:
                print(f"{self.name}, одержал победу спустя {days_counter} дней(дня)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()