a = input()
b = input()

# Try conver input to integer, otherwise say alert and quit
try:
    a = int(a)
    b = int(b)
except:
    print('Please, enter a number.')
    quit()

sum_of_two = a + b
difference = a - b
product = a * b

print(sum_of_two)
print(difference)
print(product)
