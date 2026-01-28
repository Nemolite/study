class Test:
    """ Тествоый класс"""
    def __init__(self,a,d,b):
        # public
        self.a = a
        # procected
        self._d = d
        # private
        self.__b = b

    # сеттер
    def set_b(self,b):
        self.__b = b

    # геттер
    def get_b(self):
        return self.__b

obj = Test(1,2,3)

print(obj.a)
print(obj.get_b())

obj.set_b(44)
print(obj.get_b())
