"""5....Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
При инициализации они должны принимать новый аргументы(количество колес."""

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


tr = Car(19)
tr1 = Car(15, 'kamaz', 'orange')

tr2 = Moped(3, 'ural','blue')
tr3 = Moped()
print(tr.__dict__, tr.color, tr.model, tr.wheels)
print(tr1.__dict__, tr1.color, tr1.model, tr1.wheels)
print(tr2.__dict__, tr2.color, tr2.model, tr2.wheels)
print(tr3.__dict__, tr3.color, tr3.model, tr3.wheels)