class Animal:
    def __init__(self, leg, arm):
        self.leg = leg
        self.arm = arm

    def __str__(self):
        return str('leg: ' + str(self.leg) + ', arm: ' + str(self.arm))


class Bird(Animal):
    def __init__(self, leg, wing):
        super().__init__(leg, wing)
        self.arm = wing

    def __str__(self):
        return str('leg: ' + str(self.leg) + ', wing: ' + str(self.arm))


class Fish(Animal):
    def __init__(self, plavnik):
        super().__init__(plavnik, arm=0)
        self.leg = plavnik

    def __str__(self):
        return str('plavnik: ' + str(self.leg) + ', arm/wing: ' + str(self.arm))


class Mix(Fish, Animal):
    def __init__(self, plavnik):
        super().__init__(plavnik)


elephant = Animal(4, 0)
print('elephant', elephant.leg)

eagle = Bird(2, 2)
print('eagle', eagle)

salmon = Fish(2)
print('salmon', salmon, Fish.__mro__)

wheal = Mix(2)
print('wheal', wheal)
