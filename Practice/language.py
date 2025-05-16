language = input("Enter your preference language: ")
match language.lower():
	case "javascript":
		print("your are a", language, "engineer")
	case "java":
		print("your are a", language, "engineer")
	case "python":
		print("your are a", language, "engineer")
	case _:
		print("your default here")