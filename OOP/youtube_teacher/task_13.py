# Патерны или шаблоны разработки - это общие способы решения частых задач и проблем
# Singleton Одиночка - это шаблон предоставления глобального доступа к состоянию, объект всегда один
# Monostate Моносостояние - это шаблон предоставления глобального доступа к состоянию, объекты могут быть разными
#
# Нужен для одной точки доступа к ресурсам/данным и для того чтобы ресурсоемкие задачи сделать 1 раз
# плюсы: 1 раз выполняем тяжелые задачи, имеем один вход для всей системы
# минусы: общесистемная глобальная переменная



class Singleton:
    instanse = None

    def __new__(cls):
        if Singleton.instanse is None:
            Singleton.instanse = super().__new__(cls)
            Singleton._do_work(Singleton.instanse)
        return Singleton.instanse

    def _do_work(self):
        print('do some hard work')
        # парсинг , дата Бэйс и т.д.
        self.data = 101


class Monostate:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('do some hard work')
            # парсинг , дата Бэйс и т.д.
            self.data = 101



if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)

    print(first.data)
    first.data = 102
    print(second.data)
    print(Singleton())
