from Doctor import Doctor
from MedicalRecordsSystem import MedicalRecordsSystem
from Patient import Patient

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
        patientAilment = input("Enter Patient Ailment: ")
        MedicalRecordsSystem.add_patient(Patient(patientID, patientName, patientDateOfBirth, patientContact, patientAilment))
        print("Patient Registration Complete")

    elif choice == "2":
        doctorID = input("Enter Doctor ID: ")
        doctorName = input("Enter Doctor Name: ")
        doctorSpecilization = input("Enter Doctor Specilization: ")
        doctorContact = input("Enter Doctor Contact: ")
        doctorShift = input("Enter Doctor Shift: ")
        MedicalRecordsSystem.add_doctor(Doctor(doctorID, doctorName, doctorSpecilization, doctorContact, doctorShift))
        print("Doctor Registration Complete")

    elif choice == "3":
        appointmentID = input("Enter Appointment ID: ")
        patientID = input("Enter Patient ID: ")
        appointmentDateAndTime = input("Enter Appointment Date and Time: ")
        appointmentShift = input("Enter Appointment Shift: ")
        try:
            appointment = MedicalRecordsSystem.schedule_auto_appointment(appointmentID, appointmentDateAndTime, appointmentShift)
            print("Appointment Scheduled: ")
            print(appointment.get_details())
        except Exception as e:
            print("Error: ", e)

