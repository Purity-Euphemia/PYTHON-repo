def seconds_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    second_in_seconds = second + hour_in_seconds + minute_in_seconds

    return second_in_seconds


print(seconds_since_midnight(13,30,45))