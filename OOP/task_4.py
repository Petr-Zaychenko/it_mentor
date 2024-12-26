"""4....Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства."""

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


pt = MeansOfTransport('pontiac','green')
print(pt.get_col)
pt.get_col = 'black'
print(pt.get_col)

print(pt.get_mod)
pt.get_mod = 'biches-car'
print(pt.get_mod)
