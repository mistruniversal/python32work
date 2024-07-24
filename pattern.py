"""
Фабричный метод это - пораждающий патерн проектирования который опредиляетобщий интерфейс для создания объектов в супер классе позволяя подклассам изменять тип создаваемых объектов
Прототип - патерн, параждающая объекты задает виды создоваемых объектов при помощи экземпляров прототипа
Пасредник-это певиденчиский патерн проектирования который позволяет уменьшить связанность множество классов между собой
"""


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


from typing import Dict, Optional

class WindowBase:
    def show(self) -> None:
        raise NotImplementedError()

    def hide(self) -> None:
        raise NotImplementedError()


class MainWindow(WindowBase):
    def show(self) -> None:
        print('Show MainWindow')

    def hide(self) -> None:
        print('Hide MainWindow')


class SettingWindow(WindowBase):
    def show(self) -> None:
        print('Show SettingWindow')

    def hide(self) -> None:
        print('Hide SettingWindow')


class HelpWindow(WindowBase):
    def show(self) -> None:
        print('Show HelpWindow')

    def hide(self) -> None:
        print('Hide HelpWindow')


class WindowMediator:
    def __init__(self) -> None:
        self.windows: Dict[str, Optional[WindowBase]] = {
            'main': None,
            'setting': None,
            'help': None
        }

    def show(self, win: WindowBase) -> None:
        for window in self.windows.values():
            if window is not None and window is not win:
                window.hide()
        win.show()

    def set_main(self, win: MainWindow) -> None:
        self.windows['main'] = win

    def set_setting(self, win: SettingWindow) -> None:
        self.windows['setting'] = win

    def set_help(self, win: HelpWindow) -> None:
        self.windows['help'] = win


# Создаем окна
main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

# Создаем медиатор и устанавливаем окна
med = WindowMediator()
med.set_main(main_win)
med.set_setting(setting_win)
med.set_help(help_win)

# Показать главное окно
main_win.show()  # Show MainWindow

# Показать окно настроек
med.show(setting_win)
# Hide MainWindow
# Show SettingWindow

# Показать окно помощи
med.show(help_win)
# Hide MainWindow
# Hide SettingWindow
# Show HelpWindow