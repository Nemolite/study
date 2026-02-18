class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    # def __len__(self):
    #     return self.a

    def __bool__(self):
        if self.a>self.b:
            return True
        else:
            return False



obj = Test(3,2)

if obj:
    print(f"{obj.a} больше чем {obj.b} ")
else:
    print(f"{obj.a} меньше чем {obj.b} ")












