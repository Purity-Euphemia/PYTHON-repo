def time_tuple(seconds, minutes, hours):
    seconds = seconds * 3600
    minutes = minutes * 60
    hours = seconds * 3600 + minutes * 60 + hours
    return seconds, minutes, hours

student_tuple = (23, 12, 14)
result = time_tuple(*student_tuple)
print(result)
