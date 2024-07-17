"""
Патерн(шаблон)-динамический (т.е во время выполнения а не заранее)
наделяет объект новыми возможностями и является гибкой альтернативой субклонирование в области расширения функциональности
"""

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



def benchmark(items):
    def actual_decorate(func):
        import time
        def wraper(*args,**kwargs):
            total=0
            for i in range(items):
                start=time.time()
                return_value=func(*args,**kwargs)
                end=time.time()
                total=total+(end-start)
                print(f'[*] {end-start}')
                return return_value
        return wraper
    return actual_decorate
@benchmark(items=18)
def fetch_webpage(url):
    import requests
    webpage=requests.get(url)
    return webpage.text
webpage=fetch_webpage('https://google.com')
print(webpage)