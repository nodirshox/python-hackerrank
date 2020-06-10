a = input()
b = input()

# Try convert input to interger, otherwise say alert and quit
try:
    a = int(a)
    b = int(b)
except:
    print('Please, enter only a number.')
    quit()

integer_part = int(a / b)
floating_part = a / b

print(integer_part)
print(floating_part)
