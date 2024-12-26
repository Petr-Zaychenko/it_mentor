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

    def __init__(self, wheels=4, mod='car', col='white'):
        self.count_of_wheels(wheels, mod, col)

    def __repr__(self):
        return f'Car({self.wheels},"{self.model}", "{self.color}")'

    def __str__(self):
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
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __iter__(self):
        return self

    def __next__(self):
        while self.index >= 0 and self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration



tr = Car(15,"BMW", "Black")
tr2 = Car(2,"Audi", "Pink")
tr3 = Car(4,"Lada", "Green")
moped1 = Moped(3, 'Ural', 'orange')

garage = Garage(tr, tr2, tr3)

print(tr) # __str__
print(f'{tr!r}') # __repr__

print(tr2 in garage) # __containts__
print(moped1 in garage) # __containts__

if garage: # __bool__
    print("Машины есть")
else:
    print("Машин нет")

print(len(garage)) # __len__

for car in garage:  # __iter__     # __next__
    print(f"______{car}______")