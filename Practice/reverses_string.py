def reverses_string(word):
	reversed = ""
	for count in word:
		reversed = count + reversed
	return reversed