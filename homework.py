# class TriangleChecker():
#     def __init__(self,num1,num2,num3)->None:
#             self.num1=num1
#             self.num2=num2
#             self.num3=num3
#     def is_triangle(self):
#         if type(self.num1)==str or type(self.num2)==str or type(self.num3)==str:
#             print("Нужно вводить только числа!")
#         else:
#             if self.num1%2==0 and self.num2%2==0 and self.num3%2==0 :
#                 print("Ура, можно построить треугольник!")
#             elif self.num1%2!=0 or self.num2%2!=0 or self.num3%2!=0:
#                 print("С отрицательными числами ничего не выйдет")
#             else:
#                 print("С отрицательными числами ничего не выйдет!")
# cr=TriangleChecker(2,1,6)
# print(cr.is_triangle())

# class KgToPounds():
#     def __init__(self,kg):
#         super().__init__()
#         self.kg=kg
#     def to_pounds(self):
#         return self.kg*2.204623
#     def set_kg(self):
#         def __new__(cls, *args, **kwargs):
#         newkg=input("новое значение кг")
# cr=KgToPounds(57)
# print(cr.to_pounds())