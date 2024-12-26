"""7....Попробуйте инициализировать несколько любых переменных в классе Car и сделайте одну
переменную приватной, одну защищенной. Попробуйте получить к ним доступ. Какой результат?"""


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
    def __init__(self, wheels=4, mod='car', col='white'):
        self.count_of_wheels(wheels, mod, col)



class Moped(MeansOfTransport):

    def __init__(self, wheels=2, mod='moped', col='white'):
        self.count_of_wheels(wheels, mod, col)
    @staticmethod
    def travel_time(distance, max_speed):
        tr_time = distance / max_speed
        return f"время в пути: {tr_time} ч."


tr = Car(8, 'ural', 'orange') # создаю
tr.get_col = 'red'                            # меняю цвет через сеттер
tr.get_wheels = 20                            # меняю количество колес через сеттер
print(tr.get_col, tr.get_mod, tr.get_wheels)  # вывожу без проблем через Геттер

# print(tr.__color) # не выходит обратиться
print(tr._model) # обратиться УДАЛОСЬ .
# print(tr.__wheels) # не выходит обратиться

print(tr.__dict__)
