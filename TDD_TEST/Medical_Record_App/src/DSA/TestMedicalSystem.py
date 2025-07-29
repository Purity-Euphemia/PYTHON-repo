import unittest

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
        self.patient = Patient()














if __name__ == '__main__':
    unittest.main()