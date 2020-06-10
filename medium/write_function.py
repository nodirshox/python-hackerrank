def is_leap(year):
    leap = False

    # Check leap year
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400:
            leap = False
    
    return leap
year = int(input())

result = is_leap(year)
print(result)