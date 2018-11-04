class Add:

    def __init__(self, value=0):
        self.left = value

    def get_value(self):
        return self.left

    def __add__(self, other):
        self.left += other
        return self.left


a = Add(4)
b = Add()
print(a+6)
