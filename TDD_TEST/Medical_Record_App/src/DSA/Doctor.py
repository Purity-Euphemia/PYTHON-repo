class Doctor:
    def __init__(self, doctor_id, name, specialization, contact, shif):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization.lower()
        self.contact = contact
        self.shif = shif.lower()


    def get_details(self):
        return {
            "Doctor_id": self.doctor_id,
            "Name": self.name,
            "Specialization": self.specialization.title(),
            "Contact": self.contact,
            "Shift": self.shif.title()
         }