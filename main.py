import sys
from patient import Patient
from doctor import Doctor
from room import Room
from employee import Employee
from bill import Bill
from record import Record
from user import User
from treatment import Treatment
from appointment import Appointment
from room_allocation import RoomAllocation
from medicine import Medicine  # Assuming you have a medicine module

def main():
    print("Hiii, Welcome to the Hospital Management System")
    user = User()

    while True:
        print("\nMain Menu")
        print("1. Register a new user")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            role = input("Enter role (Manager/Doctor/Patient/Receptionist/Nurse): ")
            user.register(username, password, role)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_details = user.login(username, password)
            if user_details:
                role = user_details[3]  # Extract the role from user details
                logged_in_menu(role)
            else:
                print("Login failed. Please try again.")
        elif choice == '3':
            print("Exiting...")
            user.close_connection()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def logged_in_menu(role):
    patient = Patient()
    doctor = Doctor()
    room = Room()
    employee = Employee()
    bill = Bill()
    record = Record()
    treatment = Treatment()
    appointment = Appointment()
    room_allocation = RoomAllocation()
    medicine = Medicine()  # Initialize medicine management

    while True:
        print("\nLogged-in Menu")
        if role == "Manager":
            print("1. Patient Management")
            print("2. Doctor Management")
            print("3. Room Management")
            print("4. Employee Management")
            print("5. Billing Management")
            print("6. Record Management")
            print("7. Treatment Management")
            print("8. Appointment Management")
            print("9. Room Allocation Management")
            print("10. Medicine Management")
        elif role == "Doctor":
            print("1. Patient Management")
            print("2. Room Management")
            print("3. Record Management")
            print("4. Treatment Management")
            print("5. Appointment Management")
            print("6. Medicine Management")
        elif role == "Patient":
            print("1. Personal Records")
            print("2. Billing Management")
            print("3. Appointment Management")
            print("4. Medicine Information")
        elif role == "Receptionist":
            print("1. Patient Management")
            print("2. Room Management")
            print("3. Appointment Management")
            print("4. Medicine Management")
        elif role == "Nurse":
            print("1. Patient Care Records")
            print("2. Room Management")
            print("3. Treatment Management")
            print("4. Medicine Management")  

        print("0. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            if role in ["Manager","Patient","Nurse", "Doctor", "Receptionist"]:
                patient_menu(patient)
        elif choice == '2':
            if role == "Manager":
                doctor_menu(doctor)
            elif role in ["Doctor", "Receptionist", "Nurse"]:
                room_menu(room)
            elif role == "Patient":
                billing_menu(bill)
        elif choice == '3':
            if role == "Manager":
                room_menu(room)
            elif role == "Doctor":
                record_menu(record)
            elif role == "Nurse":
                treatment_menu(treatment)
            elif role in ["Receptionist", "Patient"] :
                appointment_menu(appointment)
        elif choice == '4':
            if role == "Manager":
                employee_menu(employee)
            elif role in ["Receptionist", "Nurse","Patient"]:
                medicine_menu(medicine)
            elif role == "Doctor":
                treatment_menu(treatment)
        elif choice == '5':
            if role == "Manager":
                billing_menu(bill)
            elif role == "Doctor":
                appointment_menu(appointment)
        elif choice == '6':
            if role == "Manager":
                record_menu(record)
            elif role == "Doctor":
                medicine_menu(medicine)
        elif choice == '7':
            if role in ["Manager"]:
                treatment_menu(treatment)
        elif choice == '8':
            if role in ["Manager", "Doctor", "Receptionist", "Patient"]:
                appointment_menu(appointment)
        elif choice == '9' and role == "Manager":
            room_allocation_menu(room_allocation)
        elif choice == '10':
            if role in ["Manager", "Doctor", "Receptionist", "Nurse"]:
                medicine_menu(medicine)
        elif choice == '0':
            print("Logging out...")
            break
        else:
            print("Invalid choice or Access Denied.")

    # Close connections to the databases
    close_all_connections(patient, doctor, room, employee, bill, record, treatment, appointment, room_allocation, medicine)

def close_all_connections(*args):
    for component in args:
        component.close_connection()


def patient_menu(patient):
    while True:
        print("\nPatient Management Menu")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            sex = input("Enter sex: ")
            address = input("Enter address: ")
            contact_no = input("Enter contact number: ")
            date_admitted = input("Enter date admitted (YYYY-MM-DD): ")
            date_discharged = input("Enter date discharged (YYYY-MM-DD) or 'N/A': ")
            patient.add_patient(name, sex, address, contact_no, date_admitted, date_discharged)
        elif choice == '2':
            patients = patient.view_patients()
            for p in patients:
                print(p)
        elif choice == '3':
            pid = int(input("Enter Patient ID to update: "))
            name = input("Enter new name: ")
            sex = input("Enter new sex: ")
            address = input("Enter new address: ")
            contact_no = input("Enter new contact number: ")
            date_admitted = input("Enter new date admitted (YYYY-MM-DD): ")
            date_discharged = input("Enter new date discharged (YYYY-MM-DD) or 'N/A': ")
            patient.update_patient(pid, name, sex, address, contact_no, date_admitted, date_discharged)
        elif choice == '4':
            pid = int(input("Enter Patient ID to delete: "))
            patient.delete_patient(pid)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def doctor_menu(doctor):
    while True:
        print("\nDoctor Management Menu")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            contact_no = input("Enter contact number: ")
            doctor_type = input("Enter doctor type (Permanent/Visiting/Trainee): ") 
            speciality = input("Enter speciality: ")
            shift = input("Enter shift (Morning/Evening/Night): ")  
            doctor.add_doctor(name, contact_no, doctor_type, speciality, shift)
            print("Doctor added successfully.")
        elif choice == '2':
            doctors = doctor.view_doctors()
            if doctors:
                for d in doctors:
                    print(d)
            else:
                print("No doctors found.")
        elif choice == '3':
            did = int(input("Enter Doctor ID to update: "))
            name = input("Enter new name: ")
            contact_no = input("Enter new contact number: ")
            doctor_type = input("Enter new doctor type (Permanent/Visiting/Trainee): ")  # Updated doctor_type input
            speciality = input("Enter new speciality: ")
            shift = input("Enter new shift (Morning/Evening/Night): ")  # Added shift input for update
            doctor.update_doctor(did, name, contact_no, doctor_type, speciality, shift)
            print("Doctor updated successfully.")
        elif choice == '4':
            did = int(input("Enter Doctor ID to delete: "))
            doctor.delete_doctor(did)
            print("Doctor deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")



def room_menu(room):
    while True:
        print("\nRoom Management Menu")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Update Room")
        print("4. Delete Room")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            room_type = input("Enter room type: ")
            period = input("Enter period: ")
            room.add_room(room_type, period)
        elif choice == '2':
            rooms = room.view_rooms()
            for r in rooms:
                print(r)
        elif choice == '3':
            rid = int(input("Enter Room ID to update: "))
            room_type = input("Enter new room type: ")
            period = input("Enter new period: ")
            room.update_room(rid, room_type, period)
        elif choice == '4':
            rid = int(input("Enter Room ID to delete: "))
            room.delete_room(rid)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
def employee_menu(employee):
    while True:
        print("\nEmployee Management Menu")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            salary = float(input("Enter salary: "))
            address = input("Enter address: ")
            sex = input("Enter sex: ")
            contact_no = input("Enter contact number: ")
            nid = int(input("Enter National ID: "))
            role = input("Enter role (Doctor/Receptionist/Nurse): ")

            # If role is Doctor, ask for doctor-specific details
            if role.lower() == 'doctor':
                doctor_type = input("Enter doctor type (Permanent/Visiting/Trainee): ")
                speciality = input("Enter speciality: ")
                shift = input("Enter shift (Morning/Evening/Night): ")
                employee.add_employee(name, salary, address, sex, contact_no, nid, role, doctor_type, speciality, shift)
            else:
                employee.add_employee(name, salary, address, sex, contact_no, nid, role)
                
        elif choice == '2':
            employees = employee.view_employees()
            for emp in employees:
                print(emp)
        elif choice == '3':
            eid = int(input("Enter Employee ID to update: "))
            name = input("Enter new name: ")
            salary = float(input("Enter new salary: "))
            address = input("Enter new address: ")
            sex = input("Enter new sex: ")
            contact_no = input("Enter new contact number: ")
            nid = int(input("Enter new National ID: "))
            role = input("Enter new role: ")
            employee.update_employee(eid, name, salary, address, sex, contact_no, nid, role)
        elif choice == '4':
            eid = int(input("Enter Employee ID to delete: "))
            employee.delete_employee(eid)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def billing_menu(bill):
    while True:
        print("\nBilling Management Menu")
        print("1. Add Bill")
        print("2. View Bills")
        print("3. Update Bill")
        print("4. Delete Bill")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = int(input("Enter Patient ID: "))
            treatment = input("Enter treatment type: ")
            medicine_code = int(input("Enter medicine code: "))
            medicine_name = input("Enter medicine name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            bill.add_bill(patient_id, treatment, medicine_code, medicine_name, quantity, price)
            print("Bill added successfully.")
            
        elif choice == '2':
            bills = bill.view_bills()
            for b in bills:
                print(b)
                
        elif choice == '3':
            bill_id = int(input("Enter Bill ID to update: "))
            patient_id = int(input("Enter new Patient ID: "))
            treatment = input("Enter new treatment type: ")
            medicine_code = int(input("Enter new medicine code: "))
            medicine_name = input("Enter new medicine name: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            bill.update_bill(bill_id, patient_id, treatment, medicine_code, medicine_name, quantity, price)
            print("Bill updated successfully.")
            
        elif choice == '4':
            bill_id = int(input("Enter Bill ID to delete: "))
            bill.delete_bill(bill_id)
            print("Bill deleted successfully.")
            
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def record_menu(record):
    while True:
        print("\nRecord Management Menu")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            appointment_id = int(input("Enter Appointment ID: "))
            patient_id = int(input("Enter Patient ID: "))
            description = input("Enter description: ")
            record.add_record(appointment_id, patient_id, description)
        elif choice == '2':
            records = record.view_records()
            for r in records:
                print(r)
        elif choice == '3':
            record_id = int(input("Enter Record ID to update: "))
            appointment_id = int(input("Enter new Appointment ID: "))
            patient_id = int(input("Enter new Patient ID: "))
            description = input("Enter new description: ")
            record.update_record(record_id, appointment_id, patient_id, description)
        elif choice == '4':
            record_id = int(input("Enter Record ID to delete: "))
            record.delete_record(record_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def treatment_menu(treatment):
    while True:
        print("\nTreatment Management Menu")
        print("1. Add Treatment")
        print("2. View Treatments")
        print("3. Update Treatment")
        print("4. Delete Treatment")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            treatment_name = input("treatment_name: ")
            description = input("Enter treatment description: ")
            cost = input("Enter codt of the treatment:")
            treatment.add_treatment(treatment_name, description,cost)
        elif choice == '2':
            treatments = treatment.view_treatments()
            for t in treatments:
                print(t)
        elif choice == '3':
            treatment_id = int(input("Enter Treatment ID to update: "))
            treatment_name = input("New treatment_name: ")
            description = input("Enter new treatment description: ")
            cost = input("Enter New cost of the treatment:")
            treatment.update_treatment(treatment_id, treatment_name, description,cost)
        elif choice == '4':
            treatment_id = int(input("Enter Treatment ID to delete: "))
            treatment.delete_treatment(treatment_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def appointment_menu(appointment):
    while True:
        print("\nAppointment Management Menu")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Cancel Appointment")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            date = input("Enter appointment date and time (YYYY-MM-DD) (HH:MM): ")
            status = input("Enter status(Completed/sheduled): ")
            appointment.schedule_appointment(patient_id, doctor_id, date, status)
        elif choice == '2':
            appointments = appointment.view_appointments()
            for a in appointments:
                print(a)
        elif choice == '3':
            appointment_id = int(input("Enter Appointment ID to update: "))
            patient_id = int(input("Enter new Patient ID: "))
            doctor_id = int(input("Enter new Doctor ID: "))
            date = input("Enter new appointment date (YYYY-MM-DD)  (HH:MM): ")
            status = input("Enter status(Completed/sheduled): ")
            appointment.update_appointment(appointment_id, patient_id, doctor_id, date, status)
        elif choice == '4':
            appointment_id = int(input("Enter Appointment ID to cancel: "))
            appointment.cancel_appointment(appointment_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def room_allocation_menu(room_allocation):
    while True:
        print("\nRoom Allocation Management Menu")
        print("1. Allocate Room")
        print("2. View Allocated Rooms")
        print("3. Update Room Allocation")
        print("4. Release Room")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = int(input("Enter Patient ID: "))
            room_id = int(input("Enter Room ID: "))
            allocation_date = input("Enter allocation date (YYYY-MM-DD): ")
            end_date = input("Enter leaving date (YYYY-MM-DD):")
            room_allocation.add_allocation(patient_id, room_id, allocation_date,end_date )
        elif choice == '2':
            allocations = room_allocation.view_allocations()
            for alloc in allocations:
                print(alloc)
        elif choice == '3':
            allocation_id = int(input("Enter Allocation ID to update: "))
            patient_id = int(input("Enter new Patient ID: "))
            room_id = int(input("Enter new Room ID: "))
            allocation_date = input("Enter new allocation date (YYYY-MM-DD): ")
            end_date = input("Enter new leaving date (YYYY-MM-DD):")
            room_allocation.update_allocation(allocation_id, patient_id, room_id, allocation_date,end_date)
        elif choice == '4':
            allocation_id = int(input("Enter Allocation ID to release: "))
            room_allocation.release_room(allocation_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def medicine_menu(medicine):
    while True:
        print("\nMedicine Management Menu")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Return to Previous Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter medicine name: ")
            dosage = input("Enter medicine use: ")
            price = float(input("Enter price: "))
            medicine.add_medicine(name, dosage,price)
        elif choice == '2':
            medicines = medicine.view_medicines()
            for med in medicines:
                print(med)
        elif choice == '3':
            mid = int(input("Enter Medicine ID to update: "))
            name = input("Enter new medicine name: ")
            dosage = input("Enter medicine use: ")
            price = float(input("Enter new price: "))
            medicine.update_medicine(mid, name, dosage, price)
        elif choice == '4':
            mid = int(input("Enter Medicine ID to delete: "))
            medicine.delete_medicine(mid)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
