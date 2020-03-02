'''
# vowels -> g
#------------------
# dog -> dgg
# cat -> cgt
'''
import re

vowels = "aeiouAEIOU"

def translate(phase: str) -> str:
    output = ""
    for c in phase:
        ch = c
        if c in vowels:
            print(c)
            ch = 'g'
        output += ch

    return output

word = 'cat'
word = 'country'
word = "Hello World! On Time!"
print(translate(word))
#print(re.sub('a|e|i|o|u', 'g', word))
# regex replace
print(re.sub('[aeiou]', 'g', re.sub('[AEIOU]', 'G', word)))
