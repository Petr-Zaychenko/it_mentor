class Parent:

    max_cord = 100
    min_cord = 0
    def instance_method(self, arg):
        if self.min_cord <= arg <= self.max_cord:

            print("Это обычный метод")

    @classmethod
    def class_method(cls, arg):
        if cls.min_cord <= arg <= cls.max_cord:
            print(f"@classmethod из {cls.__name__}")
    @staticmethod
    def static_method(arg):
        if min_cord <= arg <= max_cord:
            print("@staticmethod из родительского класса")

class Child(Parent):
    pass
class Pepsi(Child):
    pass

