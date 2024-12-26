"""8....В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod,
который выводит на экран переменную car_drive"""

class MeansOfTransport:

    __color = "yellow"
    _model = "transport"

    def __init__(self, mod=_model, col=__color):
        self._model = mod
        self.__color = col

    @property
    def get_col(self):
        return self.__color

    @get_col.setter
    def get_col(self, col):
        self.__color = col

    @property
    def get_mod(self):
        return self._model

    @get_mod.setter
    def get_mod(self, mod):
        self._model = mod

    @property
    def get_wheels(self):
        return self.__wheels

    @get_wheels.setter
    def get_wheels(self, wheels):
        self.__wheels = wheels

    def count_of_wheels(self, wheels, mod, col):
        self.__wheels = wheels
        self._model = mod
        self.__color = col

class Car(MeansOfTransport):

    __car_drive = 4

    def __init__(self, wheels=4, mod='car', col='white'):
        self.count_of_wheels(wheels, mod, col)

    @classmethod
    def print_car_drive(self):
        return self.__car_drive



class Moped(MeansOfTransport):

    def __init__(self, wheels=2, mod='moped', col='white'):
        self.count_of_wheels(wheels, mod, col)

    @staticmethod
    def travel_time(distance, max_speed):
        tr_time = distance / max_speed
        return f"время в пути: {tr_time} ч."

tr = Car(15,"BMW", "Black")
print(tr.print_car_drive())