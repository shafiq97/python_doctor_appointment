from Person import Person

# Inheritance Concept
class MedicalStaff(Person):
  def __init__(self, position, hospital_address, email_address, name, telephone_number, identity_number):
    super().init(name, telephone_number, identity_number)
    self.position = position
    self.hospital_address = hospital_address
    self.email_address = email_address