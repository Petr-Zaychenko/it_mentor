"""10....Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
Реализуйте еще один класс, который будет наследоваться от класса Calculator
и перегрузите метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк."""



class Calculator:

    def positive(self, num1, num2):
        res = num1 + num2
        return res

class Concatenation(Calculator):

    def positive(self, text1, text2):
        if isinstance(text1, (int, float)) and isinstance(text2, (int, float)):
            return super().positive(text1, text2)
        elif isinstance(text1, str) and isinstance(text2, str):
            return super().positive(text1, text2)
        else:
            return super().positive(str(text1), str(text2))

b = Concatenation()

res = b.positive('hello ',20)
print(res)

res2 = b.positive(10, 20)
print(res2)

res3 = b.positive('Hello ', ' You!')
print(res3)