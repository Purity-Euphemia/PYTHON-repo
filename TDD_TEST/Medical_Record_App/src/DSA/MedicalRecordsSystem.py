from Appoinment import Appointment

class MedicalRecordsSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def find_doctor_for_ailment(self, ailment, shift):
        ailment = ailment.lower()
        shift = shift.lower()

        for doctor in self.doctors.values():
            if doctor.specialization.lower() == ailment and doctor.shift.lower() == shift:
                return doctor

        return None

    def is_doctor_available(self, doctor, datetime):
        for appointment in self.appointments.values():
            if appointment.doctor.doctor_id == doctor.doctor_id and appointment.datetime == datetime:
                return False
        return True

    def schedule_auto_appointment(self, appointment_id, patient_id, datetime, shift):
        patient = self.patients.get(patient_id)
        if not patient:
            raise ValueError('Patient not found')

        doctor = self.find_doctor_for_ailment(patient.ailment, shift)
        if doctor and self.is_doctor_available(doctor, datetime):
            appointment = Appointment(appointment_id, patient, doctor, datetime, patient.ailment)
            self.appointments[appointment.appointment_id] = appointment
            return appointment

        raise Exception('No appointment available')

    def get_appointments_report(self):
        return [patient.get_details() for patient in self.appointments.values()]

    def search_patient(self, patient_name):
        patient_name = patient_name.lower()
        result = []

        for patient in self.patients.values():
            if patient_name in patient.name.lower() or patient_name == patient.patient_id.lower():
                result.append(patient)
        return result






