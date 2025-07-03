import sqlite3

class Employee:
    def __init__(self, db_name='hospital_management.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

        # Create the 'Employee' table if it doesn't exist
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            salary REAL,
            address TEXT,
            sex TEXT,
            contact_no TEXT,
            nid INTEGER,
            role TEXT
        )
        ''')
        self.conn.commit()

    def add_employee(self, name, salary, address, sex, contact_no, nid, role, doctor_type=None, speciality=None, shift=None):
        # Insert new employee record into the table
        self.c.execute('INSERT INTO Employee (name, salary, address, sex, contact_no, nid, role) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (name, salary, address, sex, contact_no, nid, role))
        self.conn.commit()
        
        # If the role is Doctor, also add to the Doctor table
        if role.lower() == 'doctor':
            eid = self.c.lastrowid  # Get the last inserted employee ID
            self.c.execute('INSERT INTO Doctor (did, name, contact_no, doctor_type, speciality, shift) VALUES (?, ?, ?, ?, ?, ?)', 
                           (eid, name, contact_no, doctor_type, speciality, shift))
            self.conn.commit()

    def view_employees(self):
        # Retrieve all employee records from the table
        self.c.execute('SELECT * FROM Employee')
        return self.c.fetchall()

    def update_employee(self, eid, name, salary, address, sex, contact_no, nid, role):
        # Update an employee record based on the given id (eid)
        self.c.execute('''UPDATE Employee SET name = ?, salary = ?, address = ?, sex = ?, contact_no = ?, nid = ?, role = ? WHERE eid = ?''',
                       (name, salary, address, sex, contact_no, nid, role, eid))
        self.conn.commit()

    def delete_employee(self, eid):
        # Delete an employee record based on the given id (eid)
        self.c.execute('DELETE FROM Employee WHERE eid = ?', (eid,))
        self.conn.commit()

    def close_connection(self):
        # Close the database connection
        self.conn.close()
