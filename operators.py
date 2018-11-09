import sys


class Snow:
    def __init__(self, amount=15):
        self.amount = amount

    def __add__(self, other):
        self.amount += other
        return self.amount

    def __sub__(self, other):
        self.amount -= other
        return self.amount

    def __mul__(self, other):
        self.amount *= other
        return self.amount

    def __truediv__(self, other):
        try:
            self.amount /= other
        except (ZeroDivisionError, Exception):
            print('Amount of snow could not be 0')
            sys.exit()
        return round(self.amount)

    def make_snow(self, amount_in_row=5):
        if amount_in_row > self.amount:
            return print('Amount of snow in a row more than all snow')
        amount_of_rows = self.__truediv__(amount_in_row)
        print(amount_of_rows)
        for i in range(amount_of_rows):
            print('*' * amount_in_row)


snow = Snow(100)
snow.make_snow(15)
