class  Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phoneNumber

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_phone_number(self, phone_number):
        self.phoneNumber = phone_number


    def update(self, first_name, last_name, phone_number):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_phone_number(phone_number)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"
