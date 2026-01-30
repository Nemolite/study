class Person:
    """ Родительский класс """
    def __init__(self,name,w,h):
        self.__name = name
        self.w = w
        self.h = h

    @property
    def name(self):
        return self.__name

    def method(self):
        self.param = self.h-100
        if self.param==self.w:
            print(f"Ваш параметр в норме и равен = {self.param}")
        elif self.param>self.w:
            print(f"У вас лишний вес, ваш параметр = {self.param}")
        else:
            print(f"У вас недостаточный вес, ваш параметр = {self.param}")

class Men(Person):
    """ Наследник"""
    def __init__(self,name,w,h,male):
        super().__init__(name,w,h)
        self.male = male

    def method_men(self):
        print("method_men")

    def method(self):
        print("=======")

    def method_person(self):
        super().method()


obj1 = Men("Sergey",80,180,"мужчина")
print(obj1.name)
print(obj1.w)
print(obj1.h)
obj1.method()
obj1.method_men()
obj1.method_person()


class Women(Person):
    def method_women(self):
        print("method_women")

obj2 = Women("Жанна",52,150)
obj2.method()

obj1.method_men()
obj2.method_women()
