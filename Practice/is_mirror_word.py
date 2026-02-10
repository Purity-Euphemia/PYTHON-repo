def is_mirror_word(word):
	letter = letter.lower()

	for count in range(len(letter) // 2):
		if letter[count] != letter[-count -1]:
			return False
		return True