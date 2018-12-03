def palindrome():
    string = input('Enter line ')
    if string == string[::-1]:
        print('Palindrome')
    else:
        print('Not a palindrome')


palindrome()
