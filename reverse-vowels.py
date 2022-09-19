def reverse_vowels(text):
    vowels = 'aeiou'
    vowels_in_text = [c for c in text if c.casefold() in vowels]
    ans = ''
    for c in text:
        if c.casefold() in vowels:
            new_c = vowels_in_text.pop()
            ans += new_c.upper() if c.isupper() else new_c.lower()
        else:
            ans += c
    return ans

'''            
'Bongt Hulgirssen'
'Why da yee leogh? I chusa thu dooth.'
'Thisa uro thi peoplu yoe protect weth year peen!'
'Wa hid ti socrefeco e ciople uf monars te frii Balovae.'
'''
print(reverse_vowels('Bengt Hilgursson'))
print(reverse_vowels('Why do you laugh? I chose the death.'))
print(reverse_vowels('These are the people you protect with your pain!'))
print(reverse_vowels('We had to sacrifice a couple of miners to free Bolivia.'))

print(reverse_vowels('Ilkka'))