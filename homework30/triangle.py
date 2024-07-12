import code
def triangle_perimeter(a=code.default_a,b=code.default_b,c=code.default_c):
    return f'периметр треугольника {a+b+c}'
def triangle_area(a=code.default_a,b=code.default_b,c=code.default_c):
    return f'площадь треугольника {round(a*b*c/2)} формулу подходящую не нашел'