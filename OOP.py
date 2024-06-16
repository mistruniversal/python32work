#Класс- это шаблон или описание по которому создаются объекты ООП
#в ООП - класс опредиляет отрибуты(переменны) функции которые будут у объекта этого класса
#Обстракци - означает предаставление объекта или канцепции в программе с использованиемтолько необходимых харакатеристик игнорируя детали
#Инкопсуляция - это принцип согласно которому данные (переменные) и методы которые работают с этими данными оюъединены в одного объекта она также может определять ограничения доступак данным иметодам
#Наследование - это механизм который позволяет создовать новые классы на основе существующих
#Полиморфизм это возможность объектов разных классов выполнять одни и те же действия вызывая одинаковые методы но с разной реализацией
#Методы - это функции которые определены внутри класса
#Данные - это переменные которые определены внутри класса

# def funs():
#     pass
# class score:
#     pass
# print(type(1))
# print(type("1"))
# print(type(1.1))
# print(type(True))
# print(type([1,2]))
# print(type((1,2)))
# print(type({1,2}))
# print(type({1:2}))
# print(type(score))
# print(type(funs))

# class score:
#     name="Ivan"
#     age = 15
#
#     def say(self):
#         print("he")

# vasa = score()
# print(vasa.name)
# print(vasa.age)
# vasa.say()

# vasa2=score
# vasa2.name='gfa'
# print(vasa2.name)


# class score:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# person1=score("123","asdio")
# print(person1.name)
# print(person1.age)

# class person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return f"Меня зовут{self.name}"
# person1 = person("Иван")
# print(person1.name)


# class shkolnik:
#     def __init__(self,name,age,wait):
#         self.name = name
#         self.age = age
#         self.wait=wait
#         self.alll = name,age,wait
# persone=shkolnik("Elli",18,"idk")
# print(persone.alll)
#
# class transpor:
#     def __init__(self,speed,color):
#         self.speed = speed
#         self.color = color
#         self.alll = speed,color
#     def beep(self):
#         print("beep")
# class car(transpor):
#     def __init__(self,speed,color,owner):
#         super().__init__(speed,color)
#         self.owner=color,owner
#
#     def say_owner(self):
#         print(f"owner{self.owner}")
# car1=car(123,"red","ivan")
# print(car1.color)
# print(car1.speed)
# print(car1.owner)
#
# car1.beep()
# car1.say_owner()
#
# class bus(transpor):
#     def __init__(self,speed,color,seeds):
#         super().__init__(speed,color)
#         self.seeds=seeds
#     def say_seeds(self):
#         print(f"k-on,{self.seeds}")
#
# bus1=bus(123,"red",146)
# bus1.say_seeds()
#
# class sportcar(car,transpor):
#     pass
# cars=sportcar(123,"dasd",515)
# cars.beep()

# class human:
#     def __init__(self,name,age):
#         self.humanname=name
#         self.humanage=age
# class shkolnik(human):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         self.himself="Колонка"
#
# shkolnik1=shkolnik("anton",11)
# print(f"Имя школьника {shkolnik1.humanname} возраст {shkolnik1.humanage} что его делает школьником {shkolnik1.himself}")





# class car():
#     def __init__(self,model,year,money):
#         self.Audi=model
#         self.year=year
#         self.money=money
#         self.prob="300km"
# cars =car("audi","2003",2000000)
# print(f"Машина {cars.Audi} год {cars.year} Стоимость {cars.money}")
#
# class book():
#     def __init__(self,name,year,janr,money):
#         self.bookname=name
#         self.bookyear=year
#         self.janr=janr
#         self.money=money
# books=book("Путешествие к центру земли",2010,"Приключение","1000")
# print(f"Название книги {books.bookname} год выпуска {books.bookyear} жанр {books.janr} цена {books.money}")
#
# class stadion():
#     def __init__(self,name,data,country,idk,kon):
#         self.name1=name
#         self.data2=data
#         self.country3=country
#         self.idk4=idk
#         self.kon5=kon
# station=stadion("Прингфилд","19.02.1999","USA","Detroid",200000)
# print(f"Название {station.name1} дата открытия {station.data2} страна {station.country3} город {station.idk4} кол-во мест {station.kon5}")

# class car():
#     def __init__(self,args):
#         self.Audi=args[0]
#         self.year=args[1]
#         self.money=args[2]
#         self.prob=args[3]
# namelist=input("dad")
# lists=list(namelist.split())
# cars =car(lists)
# print(f"Машина {cars.Audi} год {cars.year} Стоимость {cars.money}")

# def sum1(a,b,name="Igor"):
#     ad=a+b
#     return name,ad
# print(sum1(1,2))

# class score():
#     def __init__(self,speed,color="yelow",owner=None):
#         self.scorespeed=speed
#         self.scorecolor=color
#         self.myowner=owner
#     def say_owner(self):
#         if self.myowner:
#             print(f"Владелец найден")
#         else:
#             print("no owner")
# car=score(200)
# car1=score(200,"red","dmitry")
# print(car.scorespeed , car.scorecolor , car.say_owner())
# print(car1.scorespeed , car1.scorecolor, car1.say_owner())





# class score():
#     def __init__(self,speed,color="yelow",owner=None)->None:
#         self.scorespeed=speed
#         self.scorecolor=color
#         self.myowner=owner
#     def say_owner(self):
#         if self.myowner:
#             print(f"Владелец найден")
#         else:
#             print("no owner")
# car=score(200,"blue")
# car1=score(speed=200,owner="dmitry")
# print(car.scorespeed , car.scorecolor , car.say_owner())
# print(car1.scorespeed , car1.scorecolor, car1.say_owner())



# class person():
#     age = 15
# person1=person
# print(person1.age)
# person1.age=14
# print(person1.age)

# class person():
#     _age = 15
#     def score(self):
#         print("hello")
# person1= person()
# print(person1._age)
# print(person1.score)

# class Myclass:
#     def __init__(self,name):
#         self._name=name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self,value):
#         self._name=value
# a=Myclass('Ivan')
# print(a.name)
# a.name = "sergey"
# print(a.name)

class myteamate():
    color = "purpule"
    def __init__(self,name,kn=4):
        self.hisname=name
        self.hiskn=kn
    def all(self):
        print(self.hisname , self.hiskn , self.color)
person=myteamate("medved")
print(person.hisname , person.hiskn , person.color)
person.all()
