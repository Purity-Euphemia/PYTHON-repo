HEART_RATE_PER_MINUTES = int(220)

age = int(input('Enter your age: '))

heart_rate = HEART_RATE_PER_MINUTES - age

print(heart_rate)

target_heart_rate = heart_rate * 0.5
target_heart_rateII = heart_rate * 0.85

print(target_heart_rate)
print(target_heart_rateII)

