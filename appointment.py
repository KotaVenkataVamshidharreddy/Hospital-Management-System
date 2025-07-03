import sqlite3

class Appointment:
    def __init__(self):
        self.conn = sqlite3.connect('hospital_management.db')
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS Appointment (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES Patient(pid),
            FOREIGN KEY (doctor_id) REFERENCES Doctor(did)
        )''')
        self.conn.commit()

    def add_appointment(self, patient_id, doctor_id, appointment_time, status):
        self.c.execute('INSERT INTO Appointment (patient_id, doctor_id, appointment_time, status) VALUES (?, ?, ?, ?)',
                       (patient_id, doctor_id, appointment_time, status))
        self.conn.commit()

    def view_appointments(self):
        self.c.execute('SELECT * FROM Appointment')
        return self.c.fetchall()

    def update_appointment(self, appointment_id, patient_id, doctor_id, appointment_time, status):
        self.c.execute('''
        UPDATE Appointment SET patient_id = ?, doctor_id = ?, appointment_time = ?, status = ? WHERE appointment_id = ?
        ''', (patient_id, doctor_id, appointment_time, status, appointment_id))
        self.conn.commit()

    def delete_appointment(self, appointment_id):
        self.c.execute('DELETE FROM Appointment WHERE appointment_id = ?', (appointment_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
