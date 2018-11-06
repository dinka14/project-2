class Enc:
    __field1 = 0
    field2 = 7

    def __init__(self):
        print("Class Enc __field1", Enc.__field1)

    def inc(self):
        self.__field1 += self.__field1

    def set_value(self, value):
        self.__field1 = value

    def get_value(self):
        try:
            return self.__field1
        except:
            print("No name")


print("Init for class:")
a = Enc()
print('a.field2', a.field2)
a.set_value(5)
print('a.get_value()', a.get_value())
a.inc()
print('a.get_value()', a.get_value())
