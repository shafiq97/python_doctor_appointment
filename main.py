
from Appointment import Appointment
from FlyingDoctor import FlyingDoctor
from Medical_Staff import MedicalStaff
from MobileClinic import MobileClinic
from Patient import Patient


def input_mobile_clinic_information():
    address = input("Enter address: ")
    race = input("Enter race: ")
    population = int(input("Enter population: "))
    hospital_name = input("Enter hospital name: ")
    travel_time = input("Enter travel time: ")
    transportation_type = input("Enter transportation type: ")
    mobile_clinic = MobileClinic(
        address, race, population, hospital_name, travel_time, transportation_type)
    with open("Records/MobileClinic.txt", "a") as file:
        file.write(f"Address: {mobile_clinic.address}\nRace: {mobile_clinic.race}\nPopulation: {mobile_clinic.population}\nHospital Name: {mobile_clinic.hospital_name}\nTravel Time: {mobile_clinic.travel_time}\nTransportation Type: {mobile_clinic.transportation_type}\n\n")


def input_flying_doctor_information():
    date = input("Enter date: ")
    day = input("Enter day: ")
    area = input("Enter area: ")
    time = input("Enter time: ")
    flying_doctor = FlyingDoctor(date, day, area, time)
    with open("Records/FlyingDoctor.txt", "a") as file:
        file.write(
            f"Date: {flying_doctor.date}\nDay: {flying_doctor.day}\nArea: {flying_doctor.area}\nTime: {flying_doctor.time}\n\n")


def view_appointments():
    appointment = Appointment()
    choice = int(input(
        "1. View all appointment\n 2.View appointments by name\nEnter your choice:"))
    if choice == 1:
        appointment.view_appointments()
    else:
        name = input("Enter patient name: ")
        if find_patient_by_name(name):
            appointment.view_appointments_by_name(name)
        else:
            print(f"No patient name {name} found in appointment record")


def set_appointments(name):
    doctor_name = input("Enter doctor name: ")
    nurse_name = input("Enter nurse name: ")
    appointment_date = input("Enter appointment date: ")
    service = input("Enter service: ")
    equipment_list = input("Enter equipment list: ").split(",")
    appointment = Appointment(doctor_name, nurse_name,
                              appointment_date, service, equipment_list)
    with open("Records/Appointments.txt", "a") as file:
        file.write(f"Doctor Name: {appointment.doctor_name}\nNurse Name: {appointment.nurse_name}\nAppointment Date: {appointment.appointment_date}\nService: {appointment.service}\nEquipment List: {appointment.equipment_list}\nPatient Name: {name}\n\n")


def consult_patient():
    with open("Records/Symptoms.txt", "r") as file:
        lines = file.readlines()
    print("\n\nSymptoms:")
    print("-------------------")
    for line in lines:
        print(line.strip())

    name = input("Enter patient name to consult: ")
    if (find_patient_by_name(name)):
        print("1. Schedule an appointment with this patient")
        print("2. Transport patient to nearby hospital")
        choice = int(input())
        if choice == 1:
            set_appointments(name)
    else:
        print(f"Patient name {name} not found\n\n")


def find_patient_by_name(name):
    with open("Records/Patient.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith(f"Name: {name}"):
            return True
    return False


def enter_symptoms():
    name = input("Enter name: ")
    if find_patient_by_name(name):
        symptoms = input(f"Enter the symptoms for {name}: ")
        with open("Records/Symptoms.txt", "a") as file:
            file.write(f"Name: {name}\nSymptoms: {symptoms}\n\n")
    else:
        print(f"No patient named {name} found in the records\n\n")


def register_patient():
    name = input("Enter name: ")
    identity_number = input("Enter identity card number: ")
    age = int(input("Enter age: "))
    race = input("Enter race: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    occupation = input("Enter occupation: ")
    telephone_number = input("Enter telephone number: ")
    home_address = input("Enter home address: ")
    state = input("Enter state: ")
    current_health_conditions = input("Enter current health conditions: ")
    patient = Patient(age, race, height, weight, occupation, home_address, state,
                      current_health_conditions, name, telephone_number, identity_number)

    with open("Records/Patient.txt", "r") as file:
        lines = file.readlines()
    found = False
    for line in lines:
        if line.startswith(f"Name: {name}"):
            found = True
            break
    if found:
        print("Patient with that name already exists in the records.")
    else:
        with open("Records/Patient.txt", "a") as file:
            file.write(f"Name: {patient.name}\nIdentity Number: {patient.identity_number}\nAge: {patient.age}\nRace: {patient.race}\nHeight: {patient.height}\nWeight: {patient.weight}\nOccupation: {patient.occupation}\nTelephone Number: {patient.telephone_number}\nHome Address: {patient.home_address}\nState: {patient.state}\nCurrent Health Conditions: {patient.current_health_conditions}\n\n")


def register_medical_staff():
    name = input("Enter name: ")
    identity_number = input("Enter identity card number: ")
    position = input("Enter position: ")
    hospital_address = input("Enter hospital address: ")
    email_address = input("Enter email address: ")
    telephone_number = input("Enter telephone number: ")
    medical_staff = MedicalStaff(
        position, hospital_address, email_address, name, telephone_number, identity_number)
    with open("Records/MedicalStaff.txt", "a") as file:
        file.write(f"Name: {medical_staff.name}\nIdentity Number: {medical_staff.identity_number}\nPosition: {medical_staff.position}\nHospital Address: {medical_staff.hospital_address}\nEmail Address: {medical_staff.email_address}\nTelephone Number: {medical_staff.telephone_number}\n\n")


def menu():
    print("Welcome to the Medical System")
    print("Please choose an option below:")
    print("1. Register Patient")
    print("2. Register Medical Staff")
    print("3. Enter patient symptoms")
    print("4. Consult Patient")
    print("5. View Appoinments")
    print("6. Add Flying Doctor Information")
    print("7. Add Mobile Clinic Information")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register_patient()
    elif choice == 2:
        register_medical_staff()
        pass
    elif choice == 3:
        enter_symptoms()
    elif choice == 4:
        consult_patient()
    elif choice == 5:
        view_appointments()
    elif choice == 6:
        input_flying_doctor_information()
    elif choice == 7:
        input_mobile_clinic_information()
    elif choice == 8:
        exit()
    else:
        print("Invalid choice. Please try again.")
    menu()


if __name__ == "__main__":
    menu()
