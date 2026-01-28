class Test:
    NAME_GAME ="Игровая стратегия"
    """ Тествоый класс"""
    def __init__(self,a,d,b):
        # public
        self.a = a
        # procected
        self._d = d
        # private
        self.__b = b

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self,b):
        self.__b = b


obj = Test(1,2,3.14)

print(obj.a)
print(obj.b)

obj.b=3,1415

print(obj.NAME_GAME)
print(Test.NAME_GAME)
