vowels = ['a', 'e', 'y', 'u', 'i', 'o']


def count_vowels(string):
    vowel_amount = 0
    dict_with_vowels = {}
    for j in vowels:
        each_vowel = 0
        for i in string.lower():
            if i == j:
                each_vowel += 1
                dict_with_vowels.update({str(j): each_vowel})
            else:
                dict_with_vowels.update({str(j): each_vowel})
        vowel_amount += each_vowel
    print('Vowel {}'.format(dict_with_vowels))
    print('Amount of vowels is {}'.format(vowel_amount))


count_vowels('AiIeEjeYyYyooooooooo  ')
