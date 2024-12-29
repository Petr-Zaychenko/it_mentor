"""9....Реализуйте все возможные магические методы в классе Car."""
class MeansOfTransport:

    color = "yellow"
    model = "transport"

    def __init__(self, mod=model, col=color):
        self.model = mod
        self.color = col

    @property
    def get_col(self):
        return self.color

    @get_col.setter
    def get_col(self, col):
        self.color = col

    @property
    def get_mod(self):
        return self.model

    @get_mod.setter
    def get_mod(self, mod):
        self.model = mod

    @property
    def get_wheels(self):
        return self.wheels

    @get_wheels.setter
    def get_wheels(self, wheels):
        self.wheels = wheels

    def count_of_wheels(self, wheels, mod, col):
        self.wheels = wheels
        self.model = mod
        self.color = col




class Car(MeansOfTransport):

    car_drive = 4
    def __new__(cls, *args, **kwargs):
        print(f"вызов __new__ для экземпляра класса : {cls}")
        return super().__new__(cls)
    def __init__(self, wheels=4, mod='car', col='white'):
        print("вызов __init__")
        self.count_of_wheels(wheels, mod, col)

    def __del__(self):
        print(f"Удаление экземпляра: {self}")


    def __setattr__(self, key, value):
        print(f"Присваиваем значение, и вызываем : __setattr__ : {value}")
        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        # print(f"Вызов __getattribute__  для: {item}")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"вызов __getattr__ для : {item}", end='      :   ')
    def __delattr__(self, item):
        print(f"   Вызываю  метод __delattr__ для {item}")
        object.__delattr__(self, item)

    def __add__(self, other):
        if isinstance(other, Car):
            return f"вызов __add__ / СКЛАДЫВАЕМ колеса у машин. их всего : {self.wheels + other.wheels} "
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Car):
            return f"вызов __sub__ / ВЫЧИТАЕМ колеса у машин : {self.wheels - other.wheels}"
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Car):
            return f"вызов __mul__ / УМНОЖАЕМ колеса у машин : {self.wheels * other.wheels}"
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Car):
            return f"вызов __truediv__ / ДЕЛИМ колеса у машин : {self.wheels // other.wheels}"
        return NotImplemented

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Car)):
            raise TypeError("мы сравниваем колеса из класса Car. а у тебя там что? ")
        return other if  isinstance(other, int) else other.wheels

    def __eq__(self, other):
        eq_wheels = self.__verify_data(other)
        return self.wheels == eq_wheels
    def __lt__(self,other):
        lt_wheels = self.__verify_data(other)
        return self.wheels < lt_wheels
    def __le__(self,other):
        le_wheels = self.__verify_data(other)
        return self.wheels <= le_wheels

    def __repr__(self):
        # print("вызов __repr__")
        return f'Car({self.wheels},"{self.model}", "{self.color}")'

    def __str__(self):
        # print("вызов __str__")
        return f'Машина {self.model},  {self.color}, {self.wheels}-колесная'

    def print_car_drive(self):
        return f"{self.get_wheels} колеса, цвет: {self.get_col}, марка: {self.get_mod}"

class Moped(MeansOfTransport):

    def __init__(self, wheels=2, mod='moped', col='white'):
        self.count_of_wheels(wheels, mod, col)

    @staticmethod
    def travel_time(distance, max_speed):
        tr_time = distance / max_speed
        return f"время в пути: {tr_time} ч."

class Garage:

    def __init__(self, *cars:Car):
        self.container = []
        self.container.extend(cars)
        self.index = 0

    def __repr__(self):
        return f"Garage {self.container}"

    def __contains__(self, item):
        print("вызов __contains__")
        return item in self.container

    def __bool__(self):
        print("вызов __bool__")
        return len(self.container) > 0

    def __len__(self):
        print("вызов __len__")
        return len(self.container)

    def __iter__(self):
        print("вызов __iter__")
        return self

    def __next__(self):
        print("вызов __next__")
        while self.index >= 0 and self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration



tr = Car(16,"BMW", "Black")
tr2 = Car(8,"AUDI", "red")

garage = Garage(tr)

print(tr) # __str__
print(f'{tr!r}') # __repr__

print(tr in garage) # __containts__

if garage: # __bool__
    print("Машины есть")
else:
    print("Машин нет")

print(len(garage)) # __len__

for car in garage:  # __iter__     # __next__
    print(f"______{car}______")

print(tr.not_car)
print(tr.__dict__)
del tr.color
print(tr.__dict__)

print(tr + tr2)
print(tr - tr2)
print(tr * tr2)
print(tr / tr2)

print(f'{tr == tr2}_____________________eq____________Я сравниваю колеса у машин ==')
print(f'{tr != tr2}_____________________eq____________Я сравниваю колеса у машин через !=  ')
print(f'{tr < tr2}____________lt_________Я сравниваю колеса у машин через <  ')
print(f'{tr > tr2}____________lt_________Я сравниваю колеса у машин через >  ')
print(f'{tr <= tr2}____________le_________Я сравниваю колеса у машин через <=  ')
print(f'{tr >= tr2}____________le_________Я сравниваю колеса у машин через =>  ')

print(Car.__name__)