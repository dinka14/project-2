import arrangement


w, l, h = input('Please enter length, width and height of a room without Windows and Doors ').split()
r1 = arrangement.Room(w, l, h)
print('Full square is ', r1.full_square())

amount_var = input('Please enter amount of windows and doors ')
for i in range(int(amount_var)):
    w, l = input('Please enter length and width of windows and doors ').split()
    r1.add_wd(w, l)

print('Work surface is', r1.work_surface())

w, l = input('Please enter length and width of one roll ').split()
r1.amount_of_rolls(w, l)
