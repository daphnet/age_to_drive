country = input ('Where are you from? ')
age = int(input ('How old are you? '))

if country == 'Taiwan':
    if age >= 18:
        print ('You are able to drive.')
    else:
        print ('You are not able to drive.')
elif country == 'USA':
    if age >= 16:
        print ('You are able to drive.')
    else:
        print ('You are not able to drive.')
else:
    print ('We can only check Taiwan or USA.')
