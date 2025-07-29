class Patient:
    def __init__(self, patient_id, name, date_of_birth, contact, ailment):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact = contact
        self.ailment = ailment


    def get_patient_details(self):
        return {
            "Patient ID": self.patient_id,
            "Name": self.name,
            "Date of Birth": self.date_of_birth,
            "Contact": self.contact,
            "Ailment": self.ailment,
        }
