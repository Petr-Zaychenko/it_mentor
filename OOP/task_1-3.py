"""1....Посмотрите первые 21 видео про ООП на python
https://www.youtube.com/watch?v=Z7AY41tE-3U&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E"""

"""2....Прочитайте статью по магическим методам https://habr.com/ru/articles/186608/"""


"""3.....Создайте класс MeansOfTransport }}(для определения цвета и марки машины), 
принимающий 2 аргумента при инициализации (марка и цвет транспортного средства). 
В этом классе реализуйте методы {{show_color(), выводящий на печать цвет транспортного средства и show_brand, 
для получения марки транспортного средства."""

class MeansOfTransport:

    color = "yellow"
    model = "lada-priora"

    def __init__(self, mod=model, col=color,):
        self.model = mod
        self.color = col

    def show_color(self):
        print(self.color)

    def show_brand(self):
        print(self.model)

pt = MeansOfTransport('pontiac','green')
pt2 = MeansOfTransport('ford', 'black')
pt3 = MeansOfTransport()

pt.show_color()
pt2.show_color()
pt3.show_color()
print()
pt.show_brand()
pt2.show_brand()
pt3.show_brand()


print()
print(pt.__dict__)
print(pt2.__dict__)
print(pt3.__dict__)