a = int(input())
b = int(input())
mod = int(input())

# Check mod is negative or not
if mod > 0:
    power = a**b
    power_mod = pow(a, b, mod)

    print(power)
    print(power_mod)
else:
    print("Please enter non-negative mod")
    quit()