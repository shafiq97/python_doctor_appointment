class Appointment:
    def __init__(self, doctor_name="", nurse_name="", appointment_date="", service="", equipment_list=""):
        # encapsulation (underscore variable)
        self._doctor_name = doctor_name
        self.nurse_name = nurse_name
        self.appointment_date = appointment_date
        self.service = service
        self.equipment_list = equipment_list

    def view_appointments(self):
        with open("Records/Appointments.txt", "r") as file:
            lines = file.readlines()
        print("Appointments:")
        print("-------------------")
        for line in lines:
            print(line.strip())

    def view_appointments_by_name(self, name):
        with open("Records/Appointments.txt", "r") as file:
            lines = file.readlines()
        print(lines)
        found = False
        for i in range(len(lines)):
            if name in lines[i]:
                found = True
                print(lines[i])  # Patient Name
                print(lines[i-1])  # Equipment List
                print(lines[i-2])  # Appointment Date
                print(lines[i-3])  # Service
                print(lines[i-4])  # Equipment List
                print(lines[i-5])  # Equipment List
            if not found:
                print("No appointments found with that name.")
