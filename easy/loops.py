n = input()

# Try convert input to integer, otherwise say alert and quit
try:
    n = int(n)
except:
    print('Please enter a number.')
    quit()

counter = 0
while counter < n:
    print(counter ** 2)
    counter += 1
