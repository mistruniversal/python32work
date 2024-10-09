import random
import threading
class Bank():
    def __init__(self,balance:int):
        self.balance=balance
        self.lock=threading.Lock()

    def deposit(self):
        self.lock.acquire()
        for i in range(100):
            a =random.randint(50,500)
            if self.balance>=500:
                print(f"Конечный баланс{self.balance}")
                self.lock.release()
                break
            else:
                self.balance+=a
                print(f"Баланс {self.balance} Увеличен на {a}")

    def take(self):
        self.lock.locked()
        ran=int(input("Случайное число:"))
        if ran<=self.balance:
            self.balance-=ran
            print(f"{ran} снято с баланса осталось {self.balance}")
        else:
            self.lock.acquire()
            print("Запрос откланен")
            for i in range(100):
                a = random.randint(50,500)
                if self.balance<=0:
                    self.lock.release()
                    print(f"Конечный баланс{self.balance}")
                    break
                else:
                    if (self.balance-a)<0:
                        continue
                    else:
                        self.balance-=a
                        print(f"Баланс {self.balance} уменьшен на {a}")


bk=Bank
id1=Bank(100)
id2=Bank(100)
num1=threading.Thread(target=id1.deposit(),args=(bk,))
num2=threading.Thread(target=id2.take(),args=(bk,))
num1.start()
num2.start()
print("Конец")

