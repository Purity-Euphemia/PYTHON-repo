from MedicalRecordsSystem import MedicalRecordsSystem

MedicalRecordsSystem = MedicalRecordsSystem()

def menu():
    print("\n---REAL_LIFE MEDICAL RECORDS SYSTEM---")
    print("1. Register Patient")
    print("2. Register Doctor")
    print("3. Auto Schedule Appointment")
    print("4. View Appointment")
    print("5.Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        patientID = input("Enter Patient ID: ")
        patientName = input("Enter Patient Name: ")
        patientDateOfBirth = input("Enter Patient Date of Birth(YYYY-MM-DD): ")
        patientContact = input("Enter Patient Contact: ")
