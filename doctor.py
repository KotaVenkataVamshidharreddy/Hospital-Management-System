import sqlite3

class Doctor:
    def __init__(self, db_name='hospital_management.db'):
        # Establish connection to the database
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

        # Create the 'Doctor' table if it doesn't exist
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS Doctor (
            did INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_no TEXT NOT NULL,
            doctor_type TEXT NOT NULL,
            speciality TEXT NOT NULL,
            shift TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    def add_doctor(self, eid, name, contact_no, doctor_type, speciality, shift):
        # Insert new doctor record into the table
        self.c.execute('INSERT INTO Doctor (did, name, contact_no, doctor_type, speciality, shift) VALUES (?, ?, ?, ?, ?, ?)', 
                       (eid, name, contact_no, doctor_type, speciality, shift))
        self.conn.commit()

    def view_doctors(self):
        # Retrieve all doctor records from the table
        self.c.execute('SELECT * FROM Doctor')
        return self.c.fetchall()

    def update_doctor(self, did, name, contact_no, doctor_type, speciality, shift):
        # Update a doctor record based on the given id (did)
        self.c.execute('''UPDATE Doctor SET name = ?, contact_no = ?, doctor_type = ?, speciality = ?, shift = ? WHERE did = ?''', 
                       (name, contact_no, doctor_type, speciality, shift, did))
        self.conn.commit()

    def delete_doctor(self, did):
        # Delete a doctor record based on the given id (did)
        self.c.execute('DELETE FROM Doctor WHERE did = ?', (did,))
        self.conn.commit()

    def close_connection(self):
        # Close the database connection
        self.conn.close()
