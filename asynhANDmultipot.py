# import time
# from threading import Thread
# def reming():
#     print('О чем вам напомнить')
#     text = input('Введите ваше напоминание')
#     print(f'через сколько минут')
#
#
#     """Какое время нужно показать напоминание"""
#
#
#     local_time=float(input())
#     local_time=local_time*60
#     time.sleep(local_time)
#     print(text)
# th=Thread(target=reming,args=())
# th.start()
# time.sleep(20)
# print('Поток пока работает мы можем сделать что нибудь еще\n')
import time

# """Потоки - это паралельно выполняемые задачи по умолчанию используется один поток все делается по очереди
# линейно без возможности делать несколько дел одновременно
# Процесс это один экземпляп запущенной например вкладка в браузере у каждого процесса есть своя часть кода стэк задач и выделенные ресурсы
# CPU Bount- Потоки в процессорах выполняют задачи двух основных видов
# если скорость выполнения задачи зависит от процессора
# Потоковые видео,
# Графики в играх,
# сложные математические уровнения,
# обучение ML модели
# IO Bount-операция когда скорость выполнения задачи зависит от какой то подсистемы
# Пример1:скорость запроса на сайт зависит от API сайта"""
# Пример2:скорость запроса на БД завист от нее же
# Асинхронное прогромирование идеально подходит для IO Bount"""










# import time
# from threading import Thread
# def sleep_me(num):
#     print(f'поток {num} засыпает на 5 сек\n')
#     time.sleep(5)
#     print(f'{num} проснулся')
# for i in range(10):
#     th = Thread(target=sleep_me,args=(i,))
#     th.start()

# import time
# from threading import Thread
# def score():
#     input('213')
#
# for i in range(4):
#     time.sleep(3)
#     th=Thread(target=score,args=())
#     th.start()



import time
from threading import Thread
def print_number():
    for i in range(5):
        print(f"Number {i}")
        time.sleep(3)

def print_laters():
    for i in "abcde":
        print(f'letter {i}')
        time.sleep(3)
thread1=Thread(target=print_number,args=())
thread2=Thread(target=print_laters,args=())
thread2.start()
thread1.start()