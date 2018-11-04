class Person:
    def __init__(self, name, lastname, qual=1):
        self.name = name
        self.lastname = lastname
        self.qual = qual

    def info(self):
        print("Сотрудник" + self.name + self.lastname + "имеет квалификацию" + self.qual)

    def __del__(self):
        print("До свидания, мистер {} {}".format(self.name,self.lastname))


def byQual_key(person):
    return person.qual


persons = []
persons.append(Person("Иван", "Иванов", 12))
persons.append(Person("Петр", "Петров", 5))
persons.append(Person("Сидр", "Сидоров", 3))
print(persons)

p = sorted(persons, key=byQual_key, reverse=True)

#for i in p:
#    i.info()

p[-1].__del__()

print("Press ENTER to exit")
input()