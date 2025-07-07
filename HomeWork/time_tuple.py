def function_time_tuple(seconds, minutes, hours):
    return seconds, minutes, hours


time = (9, 16, 1)
result = (function_time_tuple(*time))
print(result)
