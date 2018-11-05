import random


class Character:
    def __init__(self, number, team):
        self.number = number
        self.team = team


class Soldiers(Character):
    def go_to_hero(self, hero):
        print("Soldier {} is going to hero {}".format(self.number, hero))


class Heroes(Character):
    def __init__(self, number, team, level=1):
        Character.__init__(self, number, team)
        self.level = level

    def __str__(self):
        return str(self.number)

    def inc_level(self):
        print("Level for hero {} was increased".format(self.number))
        self.level += 1


heroA = Heroes(1, 'A')
heroB = Heroes(2, 'B')
teamAList = []
teamBList = []

for i in range(random.randint(1, 20)):
    teamAList.append(Soldiers(i, 'A'))

for i in range(random.randint(1, 20)):
    teamBList.append(Soldiers(i, 'B'))


print(len(teamAList), len(teamBList))
if len(teamAList) > len(teamBList):
    heroA.inc_level()
    print("Level for heroA", heroA.level)
else:
    heroB.inc_level()
    print("Level for heroB", heroB.level)

teamAList[0].go_to_hero(heroA)
print(teamAList[0].number, heroA.number)
