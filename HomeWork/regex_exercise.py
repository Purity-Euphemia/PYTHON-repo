import re
numbers = "123-456-7890"
pattern1 = re.findall(r'\d{3}-\d{3}-\d{4}', numbers)
print(pattern1)

email = "tolu@gmail.com"
pattern2 = re.findall(r'(^[\w@][a-z]+@gmail|yahoomail\.[a-z]+)', email)
print(pattern2)

text = "Alice and Bob are Good Friends"
pattern = re.findall(r'\b[A-Z][a-z]+\b', text)
print(pattern)

text = "Hello! How are you doing?"
pattern = re.findall(r'[A-Za-z]\w+', text)
print(pattern)