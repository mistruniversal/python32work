"""
Патерн(шаблон)-динамический (т.е во время выполнения а не заранее)
наделяет объект новыми возможностями и является гибкой альтернативой субклонирование в области расширения функциональности
"""
import random

# from  functools import  partial
# печать = print
# печать("hello")
# вывод_чего_либо=partial(печать, "вфыв")
# вывод_чего_либо()

# def print_welcom():
#     if 2==2:
#         if 1==1:
#             for i in range(1,10):
#                 print('1')
#         return
# def give_me_funk(func):
#     return func
# give_me_funk(print_welcom())

# def score1(name):
#     print(1,name)
#     print(2,name)
# def score2():
#     print(3)
# def endscore(func):
#     def give_me(name):
#         f_val=func(name)
#         score2()
#         return f_val
#     return give_me
# dicorate=endscore(score1)
# dicorate('Lava')


# def hello(name):
#     print('hello',name)
# def print_wishes():
#     print('123')
# def wishes_decorator(func):
#     def get_params(name):
#         res=func(name)
#         print_wishes()
#         return res
#     return get_params
# decorate=wishes_decorator(hello)
# decorate('ivan pedrov')





# def wishes_decorator(func):
#     def get_parance(name):
#         res=func(name)
#         print_wishes()
#         return res
#     return get_parance
#
# def print_wishes():
#     print('123')
#
# @wishes_decorator
# def hello(name):
#     print('hello',name)
#
# hello('ivan petrov')


# def benchmark(func):
#     import time
#     def wraper():
#         start=time.time()
#         func()
#         end=time.time()
#         print(f'[*] {end-start}')
#     return wraper
#
# @benchmark
# def feth_webpage():
#     import requests
#     webpage=requests.get('https://google.com')
# feth_webpage()










# def benchmark(func):
#     import time
#     def wraper(*args,**kwargs):
#         start=time.time()
#         return_value=func(*args,**kwargs)
#         end=time.time()
#         print(f'[*] {end-start}')
#         return return_value
#     return wraper
#
# @benchmark
# def feth_webpage():
#     import requests
#     webpage=requests.get(url)
#     return webpage.text
# webpage=feth_webpage('https://google.com')
# print(webpage)












# '''
# декораторы с аргументами
# '''
# def benchmark(func):
#     import time
#     def wraper(*args,**kwargs):
#         start=time.time()
#         return_value=func(*args,**kwargs)
#         end=time.time()
#         print(f'[*] {end-start}')
#         return return_value
#     return wraper
#
# @benchmark
# def feth_webpage(url):
#     import requests
#     webpage=requests.get(url)
#     return webpage.text
# webpage=feth_webpage('https://google.com')
# print(webpage)



# def benchmark(items):
#     def actual_decorate(func):
#         import time
#         def wraper(*args,**kwargs):
#             total=0
#             for i in range(items):
#                 start=time.time()
#                 return_value=func(*args,**kwargs)
#                 end=time.time()
#                 total=total+(end-start)
#                 print(f'[*] {end-start}')
#                 return return_value
#         return wraper
#     return actual_decorate
# @benchmark(items=18)
# def fetch_webpage(url):
#     import requests
#     webpage=requests.get(url)
#     return webpage.text
# webpage=fetch_webpage('https://google.com')
# print(webpage)



"""
Декоратор classmetod - функции декорированные при помощи @class метод привязывается к кслассу
 а не  объекту но они могут вызываться как из классов та и объектов экземплярова класса
"""

# class parser:
#     DOMAIN='website'
#     REMOVE_PARTS=['www','ru']
#     REPLASE_PARTS={'.':'_'}
#
#     @classmethod
#     def get_filename(cls,url:str)->str:
#         parts=url.split('/')
#         for p in cls.REMOVE_PARTS:
#             if p in parts:
#                 parts.remove(p)
# import time
# def cube_me(func):
#     starttime=time.time()
#     s=6*func
#     p=12*func
#     endtime=time.time()
#     print(f"Задача выполненна за {endtime-starttime} P={p}, S={s}")
#
# @cube_me
# def score(end):
#     return end
# print(score(6))



# from time import perf_counter
# def timer(unit='s'):
#     time_mapping={
#         's':1,
#         'ms':1000,
#         'm':1/60
#     }
#     def outher(func):
#         def inner(*args,**kwargs):
#             startime=perf_counter()
#             func(*args,**kwargs)
#             endtime=perf_counter()
#             total_time=round(endtime-startime)*time_mapping.get(unit,2)
#             print(total_time)
#         return inner
#     return outher
#
# @timer('s')
# def cube_me(max_number):
#     for number in range(max_number+1):
#         number**3
# cube_me(30000000)

# class myclass:
#     @classmethod
#     def classmethod(cls):
#         print("Привет это класс метод")
#     def unclassmetod(self):
#         print('не классный метод')
# myclass.classmethod()
# myclass.unclassmetod(1)

"""
staticmethod-Используется для создания метода который ничего не знает о классе или экземпляре через который он вызван он просто получает переданные аргументы 
без неявного первого аргумента и его опредиления не изменяемого через наследование
Простыми словами - это функция которую можно вызвать не создовая экземпляр класса
"""



# class myclass:
#     @staticmethod
#     def statik():
#         print('вызов статического метода')
# myclass.statik()


# class person():
#     @staticmethod
#     def is_about_age(age):
#         if age>18:
#             return True
#         else:
#             return False
# print(person.is_about_age(23))








# class parser:
#     DOMAIN='website'
#     REMOVE_PARTS=['www','ru']
#     REPLASE_PARTS={'.':'_'}
#
#     @classmethod
#     def get_filename(cls,url:str)->str:
#         parts=url.split('/')
#         for p in cls.REMOVE_PARTS:
#             if p in parts:
#                 parts.remove(p)
#         parts.append(cls.DOMAIN)
#         filename='_'.join(parts)
#         for kp,vp in cls.REPLASE_PARTS.items():
#             filename=filename.replace(kp,vp)
#         return filename
# url='www.sportmaster.ru/data/catalog/muzhskaya_odezhda/kurtki/'
# filename=parser.get_filename(url)
# print(filename)

# class worker:
#     @staticmethod
#     def calculate_salary(produck:float):
#         if produck<.3:
#             salary = random.randint(10000,30000)
#         elif produck<.7:
#             salary=random.randint(50000,70000)
#         elif produck<.9:
#             salary=random.randint(120000,140000)
#         else:
#             salary=random.randint(170000,210000)
#         return salary
# salary=worker.calculate_salary(produck=.785667)
# print(salary)




"""
property-вызывается в случае когда нужно вскрыть атрибуты от вмешательства из вне
для изминения потребуются getattr setattr delettr"""
# class shkolnik:
#     def __init__(self,name:str,lastname:str):
#         self.name=name
#         self.lastname=lastname
#     @property
#     def name(self):
#         return self.name
#     @name.setter
#     def name(self,lastname:str):
#         self.name=lastname
#     @name.deleter
#     def name(self):
#         del self.name
# s=shkolnik('ahot','magamed')
# s.names='alex'
# print(s.name)
# del s.name
# print(s.name)

# """
# декораторы классы
# """
#
#
# def decorator(cls):
#     class wrapper:
#         def __init__(self,*args):
#             self.wrapped=cls(*args)
#         def __getattr__(self, name):
#             return getattr(self.wrapped,name)
#     return wrapper
# @decorator
# class c:
#     def __init__(self,x,y):
#         self.attr='spam'
# b=c(6,8)
# print(b.attr)
