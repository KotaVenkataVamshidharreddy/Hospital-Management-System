import sqlite3

class Record:
    def __init__(self, db_name='hospital_management.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Record (
            record_no INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment TEXT NOT NULL,
            patient_ID INTEGER NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (patient_ID) REFERENCES Patient(pid) ON DELETE CASCADE
        )''')
        self.conn.commit()

    def add_record(self, appointment, patient_ID, description):
        self.c.execute('INSERT INTO Record (appointment, patient_ID, description) VALUES (?, ?, ?)',
                       (appointment, patient_ID, description))
        self.conn.commit()

    def view_records(self):
        self.c.execute('SELECT * FROM Record')
        return self.c.fetchall()

    def update_record(self, record_no, appointment, patient_ID, description):
        self.c.execute('''UPDATE Record SET appointment = ?, patient_ID = ?, description = ? WHERE record_no = ?''',
                       (appointment, patient_ID, description, record_no))
        self.conn.commit()

    def delete_record(self, record_no):
        self.c.execute('DELETE FROM Record WHERE record_no = ?', (record_no,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
