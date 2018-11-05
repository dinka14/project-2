import random


class Warrior:
    h = 0

    def __init__(self, name, health=100):
        self.health = health
        self.name = name

    def __str__(self):
        return str(self.name)

    def shoot(self, second_unit):
        print("{} started attack".format(self.name))
        second_unit.health -= 20
        print("{} was attacked".format(second_unit.name))
        print("{} health for {}".format(second_unit.health, second_unit.name))

    def die(self, second_unit):
        if self.health == 0:
            print("{} died".format(self.name))
            return
        elif second_unit.health == 0:
            print("{} died".format(second_unit.name))
            return
        else:
            print("One more shoot please")


unit1 = Warrior('unit1')
unit2 = Warrior('unit2')
unit_list = [unit1, unit2]

while unit1.health > 0 and unit2.health > 0:
    random_unit1 = random.randint(0, 1)
    random_unit2 = random.randint(0, 1)
    if random_unit1 == random_unit2:
        pass
    else:
        unit_list[random_unit1].shoot(unit_list[random_unit2])
        unit1.die(unit2)
