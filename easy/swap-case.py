def swap_case(s):
    new_word = ''

    for letter in range(0, len(s)):
        num = ord(s[letter])
        if num >= 65 and num <= 90:
            num += 32
        elif num >= 97 and num <= 122:
            num -= 32
        else:
            new_word += s[letter]
            continue
        
        char = chr(num) 
        new_word += char

    return new_word

string = input()
result = swap_case(string)
print(result)