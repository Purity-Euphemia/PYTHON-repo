class welcome_to_semicolon_Second:

	def __init__(self):
		self.list = []

	def add_name(self, name, hour, pay, rate1, rate2):
		if name == " ":
			return "Enter Employee name"
		if name not in self.list:
			self.list.append({"name:": name, "Enter number of hours worked in a week:": hour, "Enter Hourly pay rate:": pay, "Enter federal tax withholding rate:": rate1, "Enter state tax withholding rate:": rate2})
			return "Employee payroll add ==========>"
		return "Employee already exesits"

	def view_employee(self):
		if not self.list:
			return "No employee details added"
		result = "\nlist of employee payroll:\n"
		for count, display in enumerate(self.list, 1):
			result += f"{count}. {list['name'], ['hour'], ['pay'], ['rate1'], ['rate2']}\n"
		return result

	def update_employee_payroll(self, index):
		if 1 <= index <= len(self.list):
			employee = self.list.pop(index - 1)
			return f"Employee_payroll_list '{employee['name']}' deleted, recreate profile"
		return "hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm?!!"
	def rate1(amount):
		if pay < 0:
			return "Invalid pay"
		else:
			result = pay * 0.2
			rate1 += result
			return rate1
			return f"federal tax withholding rate (20.0%): ${rate1}"

	def rate2(pay):
		if pay < 0:
			return "Invalid pay"
		else:
			result = pay * 0.09
			rate2 += result
			return f"state tax withholding rate (9.0%): ${rate2}"


def main():
	welcome_to_semicolon_main = welcome_to_semicolon()
	while True:
		print("WELCOME TO EMPLOYEES PAYROLL");

		print("LIST OF MENU FUNTIONS");

		MENU = """
		1. Add Employee payroll.
		2. View Employees payroll.
		3. Update Employees payroll.
		4. Exits.
	
		""";
		print(MENU)
		number = input("Enter your choice (1-4): ")

		if number == "1":
			print("\nadd employee names")
			name = input("Enter Employee name: ")
			hour = float(input("Enter Number of Hours Worked: "))
			pay = float(input("Enter pay rate: "))
			Gross = hour * pay
			print(welcome_to_semicolon.add_name(name, hour, pay, rate1, rate2))
			print(welcome_to_semicolon.rate1(Gross))
			print(welcome_to_semicolon.rate2(Gross))

		elif number == "2":
			print("\nView Employees payroll")
			print(welcome_to_semicolon.view_employee())

		elif number == "3":
			print("\nupdate employee payroll")
			number = input("Enter the  ")
			print(welcome_to_semicolon.update_employee_payroll())
			try:
				num = int(input("Enter num to edit: "))
				print(welcome_to_semicolon.update_employee_payroll(num))
			except Error:
				print("Invalid number, please enter a number")

		elif number == "4":
			print("thanks")
			break
		else:
			print("enter 1 to 4 to menu")

if __name__ == "__main__":
	main()





