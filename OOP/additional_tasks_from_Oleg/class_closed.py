class Closed_class:
    __initialized = False
    def __init__(self, arg1, arg2):
        if not self.__initialized:
            self.arg1 = arg1
            self.arg2 = arg2
            type(self).__initialized = True
        else:
            raise AttributeError("Содание новых объектов запрещенно ")

    def __setattr__(self, name, value):
        if self.__initialized:
            raise AttributeError(f"Атрибут '{name}' уже установлен и не может быть изменен")
        super().__setattr__(name, value)
    def __delattr__(self, name):
        if self.__initialized:
            raise AttributeError("Удаление атрибутов запрещено")
        super().__delattr__(name)

# Создание объекта
x = Closed_class('Значение 1 ', 'Значение 2')
print(x.arg1, x.arg2)

# Попытка изменить атрибут
# x.arg1 = 'Новое значение '    # Ошибка AttributeError

# Попытка удалить атрибут
# del x.arg1                    # Ошибка AttributeError

# Попытка создать новый объект
# y = Closed_class("3", "4")



