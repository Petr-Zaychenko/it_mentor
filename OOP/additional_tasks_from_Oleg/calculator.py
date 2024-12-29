"""10....Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
Реализуйте еще один класс, который будет наследоваться от класса Calculator
и перегрузите метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк."""


class Calculator():

    def add_num(self, a, b):
        print(a + b)

class Cons(Calculator):

    def add_num(self, a=None, b=None, c=None, ):
        if a!=None and b!=None and c!=None:
            s = a + b + c
            return s
        elif a!=None and b!=None:
            s = a + b
            return s
        else:
            return a

x = Cons()
print(x.add_num(5))
print(x.add_num(5,6))
print(x.add_num(5,5, 5))
print(x.add_num('привет '))
print(x.add_num("привет ","цифра "))
print(x.add_num("привет ","цифра ", " семь"))

x = Calculator()
Calculator.add_num(x,5, 6)