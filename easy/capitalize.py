def solve(s):
    word = ''
    is_space = False
    for letter in range(0, len(s)):
        num = ord(s[letter])
        
        if is_space == True and num >= 97 and num <= 122:
            word += s[letter].upper()    
        else:
            if letter == 0:
                word += s[letter].upper()
            else:
                word += s[letter]
        
        if num == 32:
            is_space = True
        else:
            is_space = False

    return word

word = input()
result = solve(word)

print(result)
