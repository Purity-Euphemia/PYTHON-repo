def seconds_since_midnight(hour, minute, seconds):
	hour_in_seconds = 60 * 60 * hour
	minute_in_seconds = 1 * 60 * minute
	value = hour_in_seconds + minute_in_seconds + seconds

	return value

print (seconds_since_midnight(13, 30, 45))
	