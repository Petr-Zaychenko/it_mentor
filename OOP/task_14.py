"""14....Напишите класс, который принимает список людей с интерфейсом добавления
новых и при итерации возвращал имена людей"""

class People:
    def __init__(self):
        self.people_name = []
        self.index = 0

    def add_person(self, name):
        self.people_name.append(name)
    #
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.people_name):
            raise StopIteration
        result = self.people_name[self.index]
        self.index += 1
        return result


name_p = People()

name_p.add_person('Egor')
name_p.add_person('Pavel')
name_p.add_person('Anton')
name_p.add_person('Helga')

for i in name_p:
    print(i)
