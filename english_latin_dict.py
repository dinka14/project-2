from collections import defaultdict

lines = int(input())
english_dict = {}
for i in range(lines):
    line = input()
    word = line[:line.index(' - ')]
    english_dict[word] = line[len(' - ') + line.index(' - '):].split(', ')

latin_words_dict = defaultdict(list)
latin_dict = {}
for key in english_dict:
    for word in english_dict[key]:
        var = latin_words_dict[word]
        var_append = var.append(key)
        latin_dict.update({word: var})

print(len(latin_dict))
for key in sorted(latin_dict):
    print(key + ' - ' + ', '.join(sorted(latin_dict[key])))
