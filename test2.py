class Animal:
    def __init__(self, animalName, parametr2):
        print(animalName, parametr2, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName, 'e')


def method_friendly_decorator(method_to_decorate):
    def wrapper(self):
        print('That\'s an animal')
        return method_to_decorate(self)
    return wrapper


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName, parametr2):
        print(NonWingedMammalName, parametr2, "can't fly.")
        super().__init__(NonWingedMammalName)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)


class Dog(NonWingedMammal, NonMarineMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog', 'pio')

    @method_friendly_decorator
    def it_is_a_dog(self):
        print('I\'m a dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')
d.it_is_a_dog()
# test commit
