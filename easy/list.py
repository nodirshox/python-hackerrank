N = int(input())

list = []

counter = 0
while counter < N:
    command = input()
    if command.startswith('insert'):
        words = command.split()
        list.insert(int(words[1]), int(words[2]))
    elif command == 'print':
        print(list)
    elif command.startswith('remove'):
        words = command.split()
        list.remove(int(words[1]))
    elif command.startswith('append'):
        words = command.split()
        list.append(int(words[1]))
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop()
    elif command == 'reverse':
        list.reverse()
    counter += 1
