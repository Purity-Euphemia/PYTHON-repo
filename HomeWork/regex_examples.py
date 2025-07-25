import re
text = "The Silent 12 Boy, is sick23 today, call this number***090123 king456778"
pattern = re.findall(r'\w+\s+', text)
print(pattern)

pattern2 = re.findall(r'\d+', text)
print(pattern2)

pattern3 = re.findall(r'[a-z]+', text)
print(pattern3)

pattern4 = re.compile('[a-zA-Z]+]')
matches = pattern4.findall(text)
print(matches)

pattern5 = re.findall(r'\b\d+\b', text)
print(pattern5)

pattern6 = re.findall(r'[0-9]', text)
print(pattern6)

pattern7 = re.compile(r'1')
print(pattern7.findall(text))

pattern8 = re.compile(r'^CALL')
print(pattern8.findall(text))

pattern9 = re.compile(r'[^0-9]+')
print(pattern9.findall(text))