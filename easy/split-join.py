def split_and_join(text):
    splitted = text.split()
    result = '-'.join(splitted)
    return result

text = input()
result = split_and_join(text)

print(result)
