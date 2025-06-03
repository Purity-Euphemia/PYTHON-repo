print("Welcome to ATM app")

accounts = {}

def is_valid_Account_number(account_number):
	return account_number.isdigit() and len(account_number) <= 10


def create_account():
	while True:
		account_number = input("Enter new account number(up to 10 digits): ")
		if not is_valid_Account_number(account_number):
			print("Invalid account number! Must be digits only and max 10 digits")
		elif account_number in accounts:
			print("Account number already exists! Try another.")
		else:
			accounts[account_number] = 0
			print(f"Account {account_number} created with balance $0")
			break


def deposit():
	account_number =input("Enter account number to deposit money: ")
	if account_number in accounts:
		amount = float(input("Enter amount to deposit: "))
		if amount > 0:
			accounts[account_number] += amount
			print(f"${amount} deposited account {account_number}. New balance: ${accounts[account_number]}")
		else:
			print("Please enter a positive amount: ")
	else:
		print("Account number not found")


def withdraw():
	account_number = input("Enter account number to withdraw money: ")
	if account_number in accounts:
		if accounts[account_number] <= 0:
			print("Your account has no money left to withdraw")
			return
		amount = float(input("Enter withdrawal amount multiples of #500 or #1000: "))
		if amount < 500:
			print("invalid amount! Withdrawals must be in multiples of #500 or #1000")
		elif amount < 90:
			print("whithdrawal failed! You cannot withdraw more than 90% of your balance")
		else:	
			accounts[account_number] -= amount + 100
			print("transaction successful")
			print(f"${amount} withdraw from account {account_number}. Remaining balance: ${accounts[account_number]}")
	else:
		print("Account number not found")
			
			

def close_account():
	account_number = input("Enter account number to close: ")
	if account_number in accounts:
		confirm = input(f"Are you sure you want to close: ")
		if confirm == 'yes':
			del accounts[account_number]
			print(f"Account {account_number} closed successfully")
		else:
			print("Account closure canceled")
	else:
		print("Account number not found")













while True:
	print("1. create account")
	print("2. deposit")
	print("3. Withdraw money")
	print("4. Close account")
	print("5. Exist")

	choice = input("Enter your choice(1-6): ")


	if choice == '1':
		create_account()
	elif choice == '2':
		deposit()
	elif choice == '3':
		withdraw()
	elif choice == '4':
		close_account()
	elif choice == '5':
		print("Thanks for using simple bank app. Goodbye")
		break
	else:
		print("please enter a number between 1 and 7")
