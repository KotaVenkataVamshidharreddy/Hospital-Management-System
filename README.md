# 🏥 Hospital Management System

A terminal-based Hospital Management System built using **Python** and **SQLite**. The project simulates real-world operations in a hospital such as **patient management**, **appointment scheduling**, **billing**, **room allocation**, **doctor records**, **medicine tracking**, and more — all accessed via role-based login functionality.

> This was developed as part of the **DBMS Assignment** for 21AIE303.

---
![image](https://github.com/user-attachments/assets/88748da8-c117-4cb0-b674-e8ea11bfc1b0)

- If the image is not clear refer (HMS.drawio)
---
## 💡 Key Features

- 👥 Role-based access for **Manager**, **Doctor**, **Patient**, **Receptionist**, and **Nurse**
- 🩺 Full CRUD operations for:
  - Patients
  - Doctors
  - Employees
  - Medicines
  - Appointments
  - Treatments
  - Records
  - Room allocation
  - Billing
- 🗂️ SQLite used for persistent data storage across multiple entities
- 🔒 Login & Registration with password hashing using `SHA-256`
- 🖥️ Console-based user interface (menu-driven navigation)

---

## 🛠️ Modules & Structure

| File                | Responsibility                          |
|---------------------|------------------------------------------|
| `main.py`           | Main application logic and role-based menus |
| `patient.py`        | Handles patient data                     |
| `doctor.py`         | Manages doctor information               |
| `appointment.py`    | Scheduling and viewing appointments      |
| `employee.py`       | Employee (admin + doctors) operations    |
| `medicine.py`       | Add/view/update/delete medicines         |
| `record.py`         | Manages treatment and appointment records|
| `room.py`           | Add/view/update/delete room types        |
| `room_allocation.py`| Allocating/releasing hospital rooms      |
| `treatment.py`      | Add/view/update treatments and cost      |
| `bill.py`           | Generate and manage patient bills        |
| `user.py`           | Login, registration, and authentication  |

---

## 👨‍💻 User Roles & Access

Each user has specific access permissions based on their role:

| Role         | Features Available |
|--------------|--------------------|
| **Manager**  | Full access to all modules |
| **Doctor**   | Patients, Records, Appointments, Treatments, Medicines |
| **Patient**  | View Records, Billing, Appointments, Medicine Info |
| **Receptionist** | Manage Patients, Appointments, Rooms, Medicines |
| **Nurse**    | Patient Care Records, Treatments, Room, Medicines |

---

## 🧪 Sample Output

**Hiii, Welcome to the Hospital Management System**

**Main Menu:**

- Register a new user  
- Login  
- Exit  

---

### 🔐 Role-Based Dashboards

- 👨‍💼 **Manager**: Logged-in menu with full access  
- 🩺 **Doctor**: Dashboard to view patients, treatments, appointments  
- 👩‍💼 **Receptionist**: Tools for managing appointments and medicine  
- 🧾 **Patient**: Personal view with billing and appointment tracking  

---

## 🛡️ Security

- Passwords are hashed using **SHA-256** for secure login  
- Unique usernames enforced using **SQLite constraints**

---

## 💾 Database

All records are stored in a local `hospital_management.db` SQLite file  
Tables are created automatically if they don't exist at runtime

---

## 📌 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   cd hospital-management-system
   ```

2. **Run the main program:**
   ```bash
   python main.py
   ```

3. **Usage Instructions:**
   - Register a new user.
   - Log in with your credentials.
   - Start managing hospital data (patients, doctors, appointments, billing, etc.).

---

## 🎯 Future Improvements

- [ ] Add a GUI using **Tkinter** or **PyQt**
- [ ] Export patient reports to **PDF** or **Excel**
- [ ] Improve **data validation** and **exception handling**
- [ ] Build **Flask**-based web dashboards for each user role

---

## 🧑‍💻 Developed By

**Vamshi**
