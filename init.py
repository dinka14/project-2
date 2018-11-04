from operator import attrgetter


class Person:
    def __init__(self, name, surname, quality=1):
        self.name = name
        self.surname = surname
        self.quality = quality

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.quality)

    def __del__(self):
        print('Goodbye Mr.{} {}'.format(self.surname, self.name))


user1 = Person('Ivan', 'Petrov', 18)
user2 = Person('Sergey', 'Lapshin', 12)
user3 = Person('Marat', 'Odoev', 3)

user_list = [user2, user3, user1]
user_quality = []
for i in range(len(user_list)):
    user_quality.append(user_list[i].quality)

'''
for i in range(len(user_list)):
    if user_list[i].quality == min(user_quality):
        print(user_list[i], 'fired')
        user_list[i].__del__()
'''

p = sorted(user_list, key=attrgetter('quality'))

p[0].__del__()
input()
