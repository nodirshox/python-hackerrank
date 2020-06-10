n = int(input())
arr = map(int, input().split())

list = []
for number in arr:
    if number in list : continue
    list.append(int(number))

list.sort()
print(list[len(list) - 2]) # Find 2-last item in list
