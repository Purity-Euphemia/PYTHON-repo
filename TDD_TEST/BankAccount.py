class BankAccount:
	accounts = []
	
	#@classmethod
	def create_account(self,name, phone, balance=0.0):
		account = {"name": name, "phone": phone, "balance":balance}
		account.append(account)
		return account