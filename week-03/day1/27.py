z = 13
# if z is between 10 and 20 print 'Sweet!'
# if less than 10 print 'More!',
# if more than 20 print 'Less!'

if 10 < z < 20:
    print('Sweet')
elif z < 10:
    print('More')
elif z > 20:
    print('Less')
else:
    print('10 or 20')


if z > 20:
    print('Less')
elif z > 10:
    print('Sweet')
else:
    print('More')
