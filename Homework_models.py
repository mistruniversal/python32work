from django.db import models



# Задание 1,2,6
# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=255, blank=True,default='')
#
#     @classmethod
#     def create(cls):
#         cls.objects.create(name='Первая категория')
#
#     @classmethod
#     def save(cls):
#         cls.objects.create(name='Вторая категория')
#         cls.objects.create(description='Описание второй категории')
#
#     @classmethod
#     def all(cls):
#         cls.objects.filter(name='равно строке Django 4')






# Задание 3,4
# class Article(models.Model):
#     title   = models.CharField(max_length=200)
#     date    = models.DateTimeField()
#     content = models.TextField()
#     status  = models.IntegerField()
#
#     @classmethod
#     def get(cls):
#         category=cls.objects.get(id=4)
#
#     @classmethod
#     def get(cls):
#         category=cls.objects.filter(title='Django 4 для начинающих')





# Задание 5
# class Group(models.Model):
#     title       = models.CharField(max_length=200, verbose_name='Категория')
#     slug        = models.SlugField(max_length=255, unique=True, verbose_name='URL имя')
#     description = models.TextField(verbose_name='Описание')
#
#     @classmethod
#     def all(cls):
#         cls.objects.all()



# Задача 7

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name  = models.CharField(max_length=30)
#
#     @classmethod
#     def delete(cls):
#         delobj=cls.objects.get(id=7)
#         delobj.delete()


