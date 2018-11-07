import math


class Room:
    def __init__(self, x, y, z):
        try:
            float(x)
            float(y)
            float(z)
        except ValueError as e:
            print('That was not a number', e)
            return
        self.width = float(x)
        self.length = float(y)
        self.height = float(z)
        self.wd = []

    def full_square(self):
        square = 2 * self.height * (self.width + self.length)
        return square

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        new_square = Room.full_square(self)
        for i in self.wd:
            new_square -= i.square
        return new_square

    def amount_of_rolls(self, length, width):
        try:
            float(length)
            float(width)
        except ValueError as e:
            print('That was not a number', e)
            return
        work_surface = Room.work_surface(self)
        square_of_rolls = float(length) * float(width)
        try:
            amount = math.ceil(work_surface / square_of_rolls)
            print('You need {} rolls'.format(amount))
        except (ZeroDivisionError, Exception) as e:
            print('Length or width could not be 0', e)
            return


class WinDoor:
    def __init__(self, x, y):
        self.square = float(x) * float(y)


w, l, h = input('Please enter length, width and height of a room without Windows and Doors ').split()
r1 = Room(w, l, h)
print('Full square is ', r1.full_square())

amount_var = input('Please enter amount of windows and doors ')
for i in range(int(amount_var)):
    w, l = input('Please enter length and width of windows and doors ').split()
    r1.add_wd(w, l)

print('Work surface is', r1.work_surface())

w, l = input('Please enter length and width of one roll ').split()
r1.amount_of_rolls(w, l)
