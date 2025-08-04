from Contact import Contact
from PhoneBook import PhoneBook

PhoneBook = PhoneBook()
print("Welcome to the Phone Book App")

while True:
    print("1. Add a new contact")
    print("2. Search a contact")
    print("3. Update a contact")
    print("4. Search by first name")
    print("5. Search by last name")
    print("6. Delete a contact")
    print("7. Display all contacts")
    print("8. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        phone_number = input("Enter your phone number: ")
        contact = Contact(first_name, last_name, phone_number)
        phone_book = PhoneBook.add_contact(contact)
        print("Contact added successfully")

    elif choice == "2":
        print("\nEnter your phone number to search: ")
        phone_number = input("Enter your phone number: ")
        contact = PhoneBook.find_by_phone_number(phone_number)
        if contact is not None:
            print("Contact found successfully")
        else:
            print("Contact not found")

    elif choice == "3":
        print("\nEnter your phone number to update: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        phone_number = input("Enter your phone number: ")
        update_contact = Contact(first_name, last_name, phone_number)
        phone_book = PhoneBook.edit_contact(phone_number, update_contact)
        print("Contact updated successfully")

    elif choice == "4":
        print("\nEnter first name to search: ")
        first_name = input("Enter your first name: ")
        matches = PhoneBook.find_by_first_name(first_name)
        for match in matches:
            print(match.first_name)
        if not matches:
            print("Contact not found")

    elif choice == "5":
        print("\nEnter last name to search: ")
        last_name = input("Enter your last name: ")
        matches = PhoneBook.find_by_last_name(last_name)
        for match in matches:
            print(match.last_name)
        if not matches:
            print("Contact not found")

    elif choice == "6":
        print("\nEnter phone number to delete: ")
        phone_number = input("Enter your phone number: ")
        phone_book = PhoneBook.remove_contact(phone_number)
        print("Contact deleted successfully")

    elif choice == "7":
        all_contacts = PhoneBook.get_all_contacts()
        if all_contacts:
            print("\nFound contacts")
            for contact in all_contacts:
                print(contact)
        else:
            print("No contacts found")

    elif choice == "8":
        print("\nExit")
