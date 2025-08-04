class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        for contact in self.contacts:
            if contact.phone_number == contact.phone_number:
                self.contacts.remove(contact)
                return True
        return False

    def find_by_phone_number(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                return contact
        return None

    def find_by_first_name(self, first_name):
        contacts = []
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                contacts.append(contact)
                return contacts
        return None

    def find_by_last_name(self, last_name):
        contacts = []
        for contact in self.contacts:
            if contact.last_name.lower() == last_name.lower():
                contacts.append(contact)
                return contacts
        return None

    def edit_contact(self, old_phone_number, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.phone_number == old_phone_number:
                self.contacts[i] = new_contact
                return True
        return False

    def get_all_contacts(self):
        return self.contacts
