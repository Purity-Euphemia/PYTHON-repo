import unittest
from datetime import datetime

from Appoinment import Appointment
from Doctor import Doctor
from Patient import Patient
from MedicalRecordsSystem import MedicalRecordsSystem

class TestMedicalSystem(unittest.TestCase):
    def setUp(self):
        self.medical_records_system = MedicalRecordsSystem()

    def test_add_patient(self):
        self.patient = Patient("P01", "Janet", "1992-10-01", "08012345678", "toothache")
        self.medical_records_system.add_patient(self.patient)
        self.assertIn("P01", self.medical_records_system.patients)

    def test_add_doctor(self):
        self.doctor = Doctor("D01", "Dr.Tunde", "dentist", "09012345678", "Morning")
        self.medical_records_system.add_doctor(self.doctor)
        self.assertIn("D01", self.medical_records_system.doctors)

    def test_schedule_appointment(self):
        self.patient = Patient("P02", "Bob", "1988_02_2002", "07030123456", "Diabetes")
        self.doctor = Doctor("D02", "Dr jane", "Diabetes", "08014567893", "Morning")

        self.medical_records_system.add_patient(self.patient)
        self.medical_records_system.add_doctor(self.doctor)

        time = datetime(2025, 3, 20, 10, 0)
        self.appointment = self.medical_records_system.schedule_auto_appointment("A02", "P02", time, "Morning")

        self.assertIn("A02", self.medical_records_system.appointments)

    def test_search_patient(self):
        self.patient1 = Patient("P03", "Charlie", "1993_03_03", "08099998888", "")
        self.medical_records_system.add_patient(self.patient1)
        result = self.medical_records_system.search_patient("Charlie")
        self.assertEqual(len(result), 1)

    def test_search_doctor(self):
        self.doctor1 = Doctor("P03", "Dr.Chris", "ENT", "08088887777", "Morning")
        self.medical_records_system.add_doctor(self.doctor1)
        result = self.medical_records_system.search_doctor("Dr.Chris")
        self.assertEqual(len(result), 1)

    def test_appointment_report(self):
        self.medical_records_system = MedicalRecordsSystem()

        self.patient = Patient("P04", "Daisy", "1995_04_04", "08066667777", "Surgeon")
        self.doctor = Doctor("D04", "Dr.Felix", "Surgeon", "07055556666", "Morning")

        self.medical_records_system.add_patient(self.patient)
        self.medical_records_system.add_doctor(self.doctor)

        time = datetime(2025, 9, 1, 12, 0)

        self.medical_records_system.schedule_auto_appointment("A02", "P04", time, "Morning")

        report = self.medical_records_system.get_appointments_report()

        self.assertEqual(len(report), 1)
        self.assertEqual(report[0]["Purpose"], "Surgeon")


if __name__ == '__main__':
    unittest.main()