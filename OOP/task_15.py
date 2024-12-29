
"""15....Напишите класс, содержит 3 любые атрибута и при изменении
логгировать всё в консоль (при изменении старое->новое)"""


import logging

class Logi_changes:
    logging.basicConfig(level=logging.DEBUG, filename="oop_logi_changes_info.log", filemode="w", encoding='utf-8',
                         format="%(asctime)s %(levelname)s %(message)s")

    def __init__(self,first_name='Иван', last_name='Иванов', city='Москва'):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def __repr__(self): # --repr-- метод, который определяет, как объект будет представлен в виде строки
        return hex(id(self)) #hex():функция преобразует целое число(id) в строку в шестнадцатеричной системе счисления.

    @property
    def get_first_name(self):
        return self.first_name

    @get_first_name.setter
    def get_first_name(self, arg):
        logging.info(f"{self} изменил First_name с {self.first_name} на {arg}")
        self.first_name = arg

    @property
    def get_last_name(self):
        return self.last_name

    @get_last_name.setter
    def get_last_name(self, arg):
        logging.info(f"{self} изменил Last_name с {self.lastt_name} на {arg}")
        self.last_name = arg

    @property
    def get_city(self):
        return self.city

    @get_city.setter
    def get_city(self, arg):
        logging.info(f"{self} изменил City с {self.city} на {arg}")
        self.city = arg


pirs1 = Logi_changes('georg', 'fasol', 'Gagra')
pirs1.get_first_name = 'Igor'

pirs2 = Logi_changes('Tuzik', 'Lebedev', 'Moskow')
pirs2.get_first_name = 'Rubinshern'
pirs2.get_city = 'Ufa'

print(pirs1.__dict__)
print(pirs2.__dict__)
