number = input()

# Try conver input to integer, otherwise say alert and quit
try:
    number = int(number)
except:
    print("Please, enter a number.")
    quit()

if number % 2 == 1:
    print('Weird')
else:
    if number >=2 and number <=5:
        print('Not Weird')
    elif number >=6 and number <=20:
        print('Weird')
    elif number > 20:
        print('Not Weird')
    else:
        print('Not in range')
