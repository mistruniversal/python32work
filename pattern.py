"""
Фабричный метод это - пораждающий патерн проектирования который опредиляетобщий интерфейс для создания объектов в супер классе позволяя подклассам изменять тип создаваемых объектов
Прототип - патерн, параждающая объекты задает виды создоваемых объектов при помощи экземпляров прототипа
Пасредник-это певиденчиский патерн проектирования который позволяет уменьшить связанность множество классов между собой
снимок это - повиденчиский патерн повидения который позволяет сохранить и востанавливать прошлые состояния объектов
строитель это - пораждающий патрн проектирования который позволяет создовать сложные объкты пошагово сторитель дает возможно использовать один и тот же код строительства для получения разных предстовлений объектов
адаптер это- структурный патерн проектирования который позволяет объктам с вне совместимыми объектами работать вместе
Заместитель(proxy) это структурный патерн проектирования который позволяет подстовлять вместо реальных объектов специальные объекты-заменители
"""
import time

# class dokuments(object):
#     def show(self):
#         raise NotImplementedError()
# class ODFdocument(dokuments):
#     def show(self):
#         print("open dokument format")
# class MSofficedocument(dokuments):
#     def show(self):
#         print('open microsoft')
#
#
# class application(object):
#     def create_document(self,type_):
#         raise NotImplementedError()
# class myaplication(application):
#     def create_document(self,type_):
#         if type_=="odf":
#             return ODFdocument()
#         elif type_=="doc":
#             return MSofficedocument()
#         else:
#             return dokuments()
#
#
# id1=myaplication()
# id1.create_document('odf').show()
# id1.create_document('doc').show()
# try:
#     id1.create_document('pdf').show()
# except:
#     print("Переделывай")
















# import copy
# from typing import Dict,Any
# class prototype(object):
#     def __init__(self):
#         self.objects={}
#     def registar(self,name,obj):
#         self.objects[name]=obj
#     def unregister(self,name):
#         del self.objects[name]
#     def clone(self,name,attrs):
#         obj = copy.deepcopy(self.objects[name])
#         obj.__dict__.update(attrs)
#         return obj
# class bird(object):
#     pass
#
# Prototypes=prototype()
# Prototypes.registar('птица',bird())
#
# owl=prototype().clone('bird',{'name':'owl'})
# print(type(owl),owl.name)
#
# duck=prototype.clone('bird',{'name':'owl'})
# print(type(duck),duck.name)



# import copy
# from typing import Dict, Any
# class Prototype:
#     def __init__(self) -> None:
#         self.objects: Dict[str, Any] = {}
#
#     def register(self, name: str, obj: Any) -> None:
#         self.objects[name] = obj
#
#     def unregister(self, name: str) -> None:
#         del self.objects[name]
#
#     def clone(self, name: str, attrs: Dict[str, Any]) -> Any:
#         obj = copy.deepcopy(self.objects[name])
#         obj.__dict__.update(attrs)
#         return obj
# class Bird:
#     """Птица"""
#     def __init__(self, name: str = "") -> None:
#         self.name = name
#     # Создаем экземпляр прототипа
#
# prototype = Prototype()
# prototype.register('bird', Bird())
# owl = prototype.clone('bird', {'name': 'Owl'})
# print(type(owl),owl.name)


# from typing import Dict, Optional
#
# class WindowBase:
#     def show(self) -> None:
#         raise NotImplementedError()
#
#     def hide(self) -> None:
#         raise NotImplementedError()
#
#
# class MainWindow(WindowBase):
#     def show(self) -> None:
#         print('Show MainWindow')
#
#     def hide(self) -> None:
#         print('Hide MainWindow')
#
#
# class SettingWindow(WindowBase):
#     def show(self) -> None:
#         print('Show SettingWindow')
#
#     def hide(self) -> None:
#         print('Hide SettingWindow')
#
#
# class HelpWindow(WindowBase):
#     def show(self) -> None:
#         print('Show HelpWindow')
#
#     def hide(self) -> None:
#         print('Hide HelpWindow')
#
#
# class WindowMediator:
#     def __init__(self) -> None:
#         self.windows: Dict[str, Optional[WindowBase]] = {
#             'main': None,
#             'setting': None,
#             'help': None
#         }
#     def show(self, win: WindowBase) -> None:
#         for window in self.windows.values():
#             if window is not None and window is not win:
#                 window.hide()
#         win.show()
#
#     def set_main(self, win: MainWindow) -> None:
#         self.windows['main'] = win
#
#     def set_setting(self, win: SettingWindow) -> None:
#         self.windows['setting'] = win
#
#     def set_help(self, win: HelpWindow) -> None:
#         self.windows['help'] = win
#
# # Создаем окна
# main_win = MainWindow()
# setting_win = SettingWindow()
# help_win = HelpWindow()
#
# # Создаем медиатор и устанавливаем окна
# med = WindowMediator()
# med.set_main(main_win)
# med.set_setting(setting_win)
# med.set_help(help_win)
#
# # Показать главное окно
# main_win.show()  # Show MainWindow
#
# # Показать окно настроек
# med.show(setting_win)
# # Hide MainWindow
# # Show SettingWindow
#
# # Показать окно помощи
# med.show(help_win)
# # Hide MainWindow
# # Hide SettingWindow
# # Show HelpWindow






#
# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any
#
#
# class Builder(ABC):
#     """
#     Интерфейс Строителя объявляет создающие методы для различных частей объектов
#     Продуктов.
#     """
#
#     @property
#     @abstractmethod
#     def product(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_a(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_b(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_c(self) -> None:
#         pass
#
#
# class ConcreteBuilder1(Builder):
#     """
#     Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
#     конкретные реализации шагов построения. Ваша программа может иметь несколько
#     вариантов Строителей, реализованных по-разному.
#     """
#
#     def __init__(self) -> None:
#         """
#         Новый экземпляр строителя должен содержать пустой объект продукта,
#         который используется в дальнейшей сборке.
#         """
#         self.reset()
#
#     def reset(self) -> None:
#         self._product = Product1()
#
#     @property
#     def product(self) -> Product1:
#         """
#         Конкретные Строители должны предоставить свои собственные методы
#         получения результатов. Это связано с тем, что различные типы строителей
#         могут создавать совершенно разные продукты с разными интерфейсами.
#         Поэтому такие методы не могут быть объявлены в базовом интерфейсе
#         Строителя (по крайней мере, в статически типизированном языке
#         программирования).
#
#         Как правило, после возвращения конечного результата клиенту, экземпляр
#         строителя должен быть готов к началу производства следующего продукта.
#         Поэтому обычной практикой является вызов метода сброса в конце тела
#         метода getProduct. Однако такое поведение не является обязательным, вы
#         можете заставить своих строителей ждать явного запроса на сброс из кода
#         клиента, прежде чем избавиться от предыдущего результата.
#         """
#         product = self._product
#         self.reset()
#         return product
#
#     def produce_part_a(self) -> None:
#         self._product.add("PartA1")
#
#     def produce_part_b(self) -> None:
#         self._product.add("PartB1")
#
#     def produce_part_c(self) -> None:
#         self._product.add("PartC1")
#
#
# class Product1():
#     """
#     Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
#     достаточно сложны и требуют обширной конфигурации.
#
#     В отличие от других порождающих паттернов, различные конкретные строители
#     могут производить несвязанные продукты. Другими словами, результаты
#     различных строителей могут не всегда следовать одному и тому же интерфейсу.
#     """
#
#     def _init_(self) -> None:
#         self.parts = []
#
#     def add(self, part: Any) -> None:
#         self.parts.append(part)
#
#     def list_parts(self) -> None:
#         print(f"Product parts: {', '.join(self.parts)}", end="")
#
#
# class Director:
#     """
#     Директор отвечает только за выполнение шагов построения в определённой
#     последовательности. Это полезно при производстве продуктов в определённом
#     порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
#     так как клиент может напрямую управлять строителями.
#     """
#
#     def __init__(self) -> None:
#         self._builder = None
#
#     @property
#     def builder(self) -> Builder:
#         return self._builder
#
#     @builder.setter
#     def builder(self, builder: Builder) -> None:
#         """
#         Директор работает с любым экземпляром строителя, который передаётся ему
#         клиентским кодом. Таким образом, клиентский код может изменить конечный
#         тип вновь собираемого продукта.
#         """
#         self._builder = builder
#
#     """
#     Директор может строить несколько вариаций продукта, используя одинаковые
#     шаги построения.
#     """
#
#     def build_minimal_viable_product(self) -> None:
#         self.builder.produce_part_a()
#
#     def build_full_featured_product(self) -> None:
#         self.builder.produce_part_a()
#         self.builder.produce_part_b()
#         self.builder.produce_part_c()
#
#
# if __name__ == "__main__":
#     """
#     Клиентский код создаёт объект-строитель, передаёт его директору, а затем
#     инициирует процесс построения. Конечный результат извлекается из объекта-
#     строителя.
#     """
#
#     director = Director()
#     builder = ConcreteBuilder1()
#     director.builder = builder
#
#     print("Standard basic product: ")
#     director.build_minimal_viable_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     print("Standard full featured product: ")
#     director.build_full_featured_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     # Помните, что паттерн Строитель можно использовать без класса Директор.
#     print("Custom product: ")
#     builder.produce_part_a()
#     builder.produce_part_b()
#     builder.product.list_parts()









# class Target:
#     """
#     Целевой класс объявляет интерфейс, с которым может работать клиентский код.
#     """
#
#     def request(self) -> str:
#         return "Target: The default target's behavior."
#
#
# class Adaptee:
#     """
#     Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
#     несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
#     некоторой доработке, прежде чем клиентский код сможет его использовать.
#     """
#
#     def specific_request(self) -> str:
#         return ".eetpadA eht fo roivaheb laicepS"
#
#
# class Adapter(Target, Adaptee):
#     """
#     Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
#     интерфейсом благодаря множественному наследованию.
#     """
#
#     def request(self) -> str:
#         return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
#
#
# def client_code(target: "Target") -> None:
#     """
#     Клиентский код поддерживает все классы, использующие интерфейс Target.
#     """
#
#     print(target.request(), end="")
#
#
# if __name__ == "__main__":
#     print("Client: I can work just fine with the Target objects:")
#     target = Target()
#     client_code(target)
#     print("\n")
#
#     adaptee = Adaptee()
#     print("Client: The Adaptee class has a weird interface. "
#           "See, I don't understand it:")
#     print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
#
#     print("Client: But I can work with it via the Adapter:")
#     adapter = Adapter()
#     client_code(adapter)




from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так
    и для Заместителя. Пока клиент работает с Реальным Субъектом, используя этот
    интерфейс, вы сможете передать ему заместителя вместо реального субъекта.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
    Реальные Субъекты способны выполнять некоторую полезную работу, которая к
    тому же может быть очень медленной или точной – например, коррекция входных
    данных. Заместитель может решить эти задачи без каких-либо изменений в коде
    Реального Субъекта.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    """
    Интерфейс Заместителя идентичен интерфейсу Реального Субъекта.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self.__real_subject = real_subject

    def request(self) -> None:
        """
        Наиболее распространёнными областями применения паттерна Заместитель
        являются ленивая загрузка, кэширование, контроль доступа, ведение
        журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
        в зависимости от результата, передать выполнение одноимённому методу в
        связанном объекте класса Реального Субъекта.
        """

        if self.check_access():
            self.__real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    """
    Клиентский код должен работать со всеми объектами (как с реальными, так и
    заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
    работают с реальными субъектами напрямую. В этом случае, для более простой
    реализации паттерна, можно расширить заместителя из класса реального
    субъекта.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

    
"""https://refactoringguru.cn/design-patterns#intro-patterns"""