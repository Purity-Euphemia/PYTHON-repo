import re
from datetime import datetime
from medical_system import MedicalSystem
from doctor import Doctor
from patient import Patient

medical_sys = MedicalSystem()
patient_list = {}

message = """
Welcome to Medical System
=========================
press 1 to Add a Doctor
press 2 to Add a Patient
press 3 to Create Appointment
press 4 to View all Appointments
press 5 to cancel Appointment
press 6 to Reschedule Appointment
press 7 to get Appointments
press 8 to find Doctor Records
press 9 to find Patient Records
press 10 to view all Patients
press 11 to view all Doctors
press 0 to Exit
"""

while True:
    print(message)
    user_input = input()
    print()
    match user_input:
        case "1":
            print("Add Doctor")
            contact_info = {}
            while True:
                name = input("Enter Doctor's full Name: ")
                if isinstance(name, str) and name.strip():
                    break
                print("Invalid name input. Doctor name can't be empty.")

            while True:
                specialisation = input("Enter Doctor's Specialisation: ")
                if isinstance(specialisation, str) and specialisation.strip():
                    break
                print("Invalid specialisation input. Doctor specialty can't be empty.")

            while True:
                phone = input("Enter Doctor's Phone Number which must be 11 digit and it must either begin with(070,080,081,090,071,091): ")
                if re.match(r"^(070|080|081|090|071|091)[0-9]{8}$", phone):
                    break
                print("Invalid phone number format. Please try again.")

            while True:
                email = input("Enter Doctor's Email Address: ").strip()
                if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
                    break
                print("Invalid email format. check and try again.")

            while True:
                address = input("Enter Doctor's Address: ")
                if isinstance(address, str) and address.strip():
                    break
                print("Invalid address, address can't be empty.")

                contact_info["phone"] = phone
                contact_info["email"] = email
                contact_info["address"] = address
            try:
                doctor = Doctor(name=name, specialisation=specialisation, contact_info=contact_info)
                medical_sys.add_doctor(doctor)
                print(doctor)
            except ValueError:
                print("invalid input... check and try again.\n")

        case "2":
            print("Add Patient")
            contact_info = {}
            while True:
                p_name = input("Enter Patient's Full Name: ")
                if isinstance(p_name, str) and p_name.strip():
                    break
                print("Invalid name. Patient name cannot be empty.")

            while True:
                date_of_birth = input("Enter Patient's Date of Birth(DD/MM/YYYY): ").strip()
                try:
                    date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
                    dob = date_of_birth.strftime('%d/%m/%Y')
                    break
                except ValueError:
                    print("Date of birth must be in DD/MM/YYYY format(eg, 10/05/2000)")
            while True:
                problem = input("Enter the patient problem: ")
                if isinstance(problem, str) and problem.strip():
                    break
                print("Invalid problem input, shouldn't be an empty String. Try again.")

            while True:
                specialty_needed = input("Enter the patient specialty needed: ")
                if isinstance(specialty_needed, str) and specialty_needed.strip():
                    break
                print("Invalid speciality needed input, speciality needed can't be an empty String. Try again.")

            while True:
                phone = input("Enter Patient's Phone Number which must be 11 digit and it must either begin with(070,080,081,090,071,091): ")
                if re.match(r"^(070|080|081|090|071|091)[0-9]{8}$", phone):
                    break
                print("Invalid phone number format. Please try again.")


            while True:
                email = input("Enter Patient's Email Address: ")
                if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
                    break
                print("Invalid email format. Please try again.")

            while True:
                address = input("Enter Patient's Address: ")
                if isinstance(address, str) and address.strip():
                    break
                print("Invalid address, address cannot be empty. Try again.")

            contact_info["phone"] = phone
            contact_info["email"] = email
            contact_info["address"] = address

            try:
                new_patient = Patient(name=p_name, dob=dob, problem=problem, speciality_needed=specialty_needed, contact_info=contact_info)
                medical_sys.add_patient(new_patient)
                patient_list[new_patient.get_id] = new_patient
                print(new_patient)
            except ValueError:
                print("Oga...go back and enter the correct details.\n")


        case "3":
            print("Create Appointment")
            try:
                pid = input("Enter Patient ID: ").strip()
                schedule_date = input("Enter Appointment date in DD/MM/YYYY HH:MM format(eg, 10/05/2000 03:00): ").strip()
                schedule_date_dt = datetime.strptime(schedule_date, '%d/%m/%Y %H:%M')
                if schedule_date_dt < datetime.now():
                    raise ValueError("Appointment date cannot be in the past")
                schedule_date = schedule_date_dt.strftime('%d/%m/%Y %H:%M')
                patient = patient_list.get(pid)
                if patient:
                    result = medical_sys.assign_doctor_to_patient(patient, schedule_date)
                    print(result)
                else:
                    print("Patient not found.")
            except ValueError as e:
                print(f"Error: {e}\nTry again.\n")

        case "4":
            print("View all Appointments")
            medical_sys.view_all_appointments()

        case "5":
            print("Cancel Appointment")
            while True:
                pid = input("Enter Patient ID: ")
                if isinstance(pid, str) and pid.strip():
                    break
                print("Invalid Patient ID. Patient ID cannot be empty.")

            try:
                date = input("Enter Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                date_format = datetime.strptime(date, '%d/%m/%Y %H:%M')
                cancel_date = date_format.strftime('%d/%m/%Y %H:%M')
                result = medical_sys.cancel_appointment(pid, cancel_date)
                print(result)
            except ValueError:
                print("Appointment date must be in DD/MM/YYYY HH:MM format")

        case "6":
            print("Reschedule Appointment")
            while True:
                try:
                    pid = input("Enter Patient ID: ").strip()
                    old_date = input("Enter old Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                    datetime.strptime(old_date, "%d/%m/%Y %H:%M")
                    new_date = input("Enter new Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                    datetime.strptime(new_date, "%d/%m/%Y %H:%M")
                    result = medical_sys.reschedule_appointment(pid, old_date, new_date)
                    print(result)
                    break
                except ValueError:
                    print("Try again.\n")

        case "7":
            print("Get Appointment")
            pid = input("Enter Patient ID: ").strip()
            result = medical_sys.get_appointment(pid)
            print(result)

        case "8":
            print("Find Doctor Record")
            did = input("Enter Doctor ID: ").strip()
            result = medical_sys.find_doctor_record(did)
            print(result)


        case "9":
            print("Find Patient Record")
            pid = input("Enter Patient ID: ").strip()
            result = medical_sys.find_patient_record(pid)
            print(result)

        case "10":
            print("View all Patients")
            medical_sys.view_all_patients()

        case "11":
            print("View all Doctors")
            medical_sys.view_all_doctors()

        case "0":
            print("Exiting the Medical System. Goodbye!")
            break


        case _:
            print("Invalid option. Please try again.")








# medical_system = MedicalSystem()
# pat_me = Patient('oni', '10/05/2000', 'chest pain', 'Cardiology', {'phone number': '1234567809', 'email': 'lizzbet110@gmail.com', 'home address': '12 Broad str'})
# pat = Patient('oni', '10/05/2000', 'chest pain', 'Cardiology', {'phone number': '1234567809', 'email': 'lizzbet110@gmail.com', 'home address': '12 Broad str'})
# medical_system.add_patient(pat)
# medical_system.add_patient(pat_me)
# dr_zeus = Doctor('Dr. Ola', "Cardiology", {'phone number': '1234567809', 'email': 'lizzbet110@gmail.com', 'home address': '12 Broad str'})
# medical_system.add_doctor(dr_zeus)
# print(str(dr_zeus))
# print(str(pat_me))
# print(str(pat))



 # appointment_day_length = 3
                    # today = datetime.today()
                    # appointment_date = today + timedelta(days=random.randint(1, appointment_day_length))
                    # hour = random.randint(9, 15)
                    # min = random.randint(0, 59)
                    # appointment_d_t = appointment_date.replace(hour=hour, minute=min, second=0, microsecond=0)
                    # appointment_d_t = appointment_d_t.strftime('%d/%m/%Y %H:%M %p')
                    # medical_sys.assign_doctor_to_patient(patient, appointment_d_t)