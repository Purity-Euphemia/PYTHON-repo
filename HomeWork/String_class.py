#text = "lion King"
#text_aligned = f'[{text:^10}]'
#print(text_aligned)
#print(len(text_aligned))
from re import Match

text = "  {lion King}  "
print(' '.format(text))

num1 = 567
num2 = 39.980

print('{:.1f}'.format(num1, num2))
print('{:d} \t{:.2f}'.format(num1, num2))

fruit = 'banana'
print(fruit*4)

fruit = '*' #  * mulpiplication of characters
print(fruit*10)

fruit = 'banana of food'
print('-'.join(fruit))

fruit = ['banana', 'of', 'food']
print('-'.join(fruit))

place = 'jungle, race, on'
print(place.strip(' '))


place = ' \t\tjungle \t\t '
print(place)
print(place.strip())

name = 'chief okafor'
print(name.capitalize())

name = 'chief okafor'
print(name.upper())

name = 'chief okafor'
print(name.lower())

name = 'chief okafor'
print(name.title())

print('cat' > 'dog')
print('cat' > 'car')

word = 'polymorphism'
print(word.find('morph')) # index of the first element
print(word.index('morph'))

word = "Time bound"
print(word.split())

word = "Time bound".split()
print(word)
print("-".join(word))

raw_str = r"C:\Users\Name"
print(raw_str)

import re
pattern = '02215'
print('Match'if re.fullmatch(pattern, '02215') else 'Not match')
print(True if re.fullmatch(pattern, '02215') else False)

import re

text = "abc123xyz"
s = re.sub(r"\d+", "-", text)
print(s)

import re

pattern = 'yahoo.com'
text = 'oba@yahoo.com'
replacement = 'gmail.com'
result = re.sub(pattern, replacement, text)
print(result)

text = "abc123xyz"
s = re.split(r'\d+', text)
print(s)

text = "letter story comprehension"
pattern = ' '
print(re.split(pattern, text))

money = '80.00,000.00.00'
pattern = ','
pattern_two = ','
first_match = re.split(pattern, money)
print(first_match)
result_in_str = ''.join(first_match)
print(type(result_in_str))
result = re.sub(pattern_two, '.', result_in_str)
print(result)

re.search(r"\d+", "abc123xyz")
print(re.search(r"\d+", "abc123xyz").group())










