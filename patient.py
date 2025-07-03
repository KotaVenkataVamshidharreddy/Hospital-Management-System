import sqlite3

class Patient:
    def __init__(self, db_name='hospital_management.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Patient (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex TEXT,
            address TEXT,
            contact_no TEXT,
            date_admitted TEXT,
            date_discharged TEXT
        )''')
        self.conn.commit()

    def add_patient(self, name, sex, address, contact_no, date_admitted, date_discharged):
        self.c.execute('INSERT INTO Patient (name, sex, address, contact_no, date_admitted, date_discharged) VALUES (?, ?, ?, ?, ?, ?)', 
                       (name, sex, address, contact_no, date_admitted, date_discharged))
        self.conn.commit()

    def view_patients(self):
        self.c.execute('SELECT * FROM Patient')
        return self.c.fetchall()

    def update_patient(self, pid, name, sex, address, contact_no, date_admitted, date_discharged):
        self.c.execute('''UPDATE Patient SET name = ?, sex = ?, address = ?, contact_no = ?, date_admitted = ?, date_discharged = ? WHERE pid = ?''', 
                       (name, sex, address, contact_no, date_admitted, date_discharged, pid))
        self.conn.commit()

    def delete_patient(self, pid):
        self.c.execute('DELETE FROM Patient WHERE pid = ?', (pid,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
