"""6....В классе {{Moped}}напишите статическую функцию, которая на вход будет принимать
расстояние и максимальную скорость, а на выходе получать время, за которое проедет мопед это расстояние."""


class MeansOfTransport:

    color = "yellow"
    model = "transport"

    def __init__(self, mod=model, col=color,):
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

    def count_of_wheels(self, wheels, mod, col):
        self.wheels = wheels
        self.model = mod
        self.color = col

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


tr = Car(18)
tr1 = Moped(3, 'ural', 'orange')

res_time = Moped.travel_time(200, 50)

print(res_time)