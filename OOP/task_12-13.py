"""12....Прочитайте статью и выполните действия, которые в ней прописаны
https://pythonist.ru/vvedenie-v-mnozhestvennoe-nasledovanie-i-super/

                        ПРОЧИТАНО """

"""13....Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс и 
какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton
Пример: https://pythonpip.ru/osnovy/shablon-proektirovaniya-singleton-v-python"""

class Dog:
    instance = None

    def __new__(cls, *args, **kwargs):
        if Dog.instance is None:
            Dog.instance = super().__new__(cls)
        return Dog.instance

    def __init__(self, nickname=" ??? ", age=0, breed='no breed', name_dog_lord='no lord'):
        self.nickname = nickname
        self.breed = breed
        self.age = age
        self.name_dog_lord = name_dog_lord
        self.greeting()

    def greeting(self):
        print(f"Привет, меня зовут {self.nickname}, мне {self.age} лет, и я {self.breed}, моего хозяина зовут {self.name_dog_lord}\n")

    def play(self):
        print("я сейчас играю \n")

    def eat_and_drink(self):
        print("я сейчас ем и пью\n")

    def shedding(self):
        print("я линяю \n")

    def follow_the_commands(self):
        print("Я выполняю команды\n")

    def barking_at_the_bikes(self):
        print("я Лаю на велосипеды WOF-WOF-WOF-WOF\n")

dog1 = Dog("Руби", 12, "Корги", "Петя")
dog1.barking_at_the_bikes()

dog2 = Dog("Ачи", 5, "Овчарка", "Рома")
dog2.play()

dog1.greeting()

print(dog1 is dog2)
print(dog1)
print(dog2)