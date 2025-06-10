print("Welcome to simple bank app")

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
		amount = float(input("Enter amount to withdraw: "))
		if amount <= 0:
			print("Please enter a positive amount")
		elif amount > accounts[account_number]:
			print("Insufficient funds")
		else:	
			accounts[account_number] -= amount
			print(f"${amount} withdraw from account {account_number}. Remaining balance: ${accounts[account_number]}")
	else:
		print("Account number not found")


def transfer():
	from_account = input("Enter your account number (from): ")
	to_account = input("Enter account number to transfer to: ")
	if from_account not in accounts:
		print(f"Account '{from_account}' not found")
		return
	if to_account not in accounts:
		print(f"Account '{to_account}' not found")
		return
	amount = float(input("Enter amount to transfer: "))
	if amount <= 0:
		print("Please enter a positive amount.")
	elif amount > accounts[from_account]:
		print("insufficiient funds to transfer")
	else:
		accounts[from_account] -= amount
		accounts[to_account] += amount
		print(f"${amount} transferred from {from_account} to {to_account}")
		print(f"${from_account} remaining balance: ${accounts[from_account]}")
		print(f"${to_account} new balance: ${accounts[to_account]}")


def show_account():
	if accounts:
		print("list of accounts and balances: ")
		for account_number, balance in accounts.items():
			print(f"- Account {account_number}: ${balance}")
	else:
		print("No accounts created yet")

def show_account_numbers():
	if accounts:
		print("Account numbers:")
		for account_number in accounts.keys():
			print(f"-{account_number}")
	else:
		print("No accounts created yet")


def show_account_details():
	account_number = input("Enter account number to view details: ")
	if account_number in accounts:
		print(f"Account {account_number} balance: ${accounts[account_number]}")
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
	print("\nChoose an option:")
	print("1. Create account")
	print("2. Deposit money")
	print("3. Withdraw money")
	print("4. Transfer money")
	print("5. Show account")
	print("6. Show account number")
	print("7. Show account details")
	print("8. Close account")
	print("9. Exist")

	choice = input("Enter your choice(1-9): ")

	if choice == '1':
		create_account()
	elif choice == '2':
		deposit()
	elif choice == '3':
		withdraw()
	elif choice == '4':
		transfer()
	elif choice == '5':
		show_accounts()
	elif choice == '6':
		show_account_numbers()
	elif choice == '7':	
		show_account_details()
	elif choice == '8':
		close_account()
	elif chioce == '9':
		print("Thanks for using simple bank app. Goodbye")
	else:
		print("invalid choice, please enter a number between 1 and 9")
	

		




















































































