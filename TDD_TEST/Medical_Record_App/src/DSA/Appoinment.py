class Appointment:
    def __init__(self, appointment_id, patient, doctor, datetime, purpose):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.datetime = datetime
        self.purpose = purpose

    def get_details(self):
        return {"Appointment ID": self.appointment_id,
                "Patient": self.patient.name,
                "Doctor": self.doctor.name,
                "Date and time": self.datetime,
                "Purpose": self.purpose
        }

