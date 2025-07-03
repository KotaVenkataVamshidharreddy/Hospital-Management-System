import sqlite3

class RoomAllocation:
    def __init__(self):
        self.conn = sqlite3.connect('hospital_management.db')
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS RoomAllocation (
            allocation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            room_id INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES Patient(pid),
            FOREIGN KEY (room_id) REFERENCES Room(rid)
        )''')
        self.conn.commit()

    def add_allocation(self, patient_id, room_id, start_date, end_date):
        self.c.execute('INSERT INTO RoomAllocation (patient_id, room_id, start_date, end_date) VALUES (?, ?, ?, ?)',
                       (patient_id, room_id, start_date, end_date))
        self.conn.commit()

    def view_allocations(self):
        self.c.execute('SELECT * FROM RoomAllocation')
        return self.c.fetchall()

    def update_allocation(self, allocation_id, patient_id, room_id, start_date, end_date):
        self.c.execute('''
        UPDATE RoomAllocation SET patient_id = ?, room_id = ?, start_date = ?, end_date = ? WHERE allocation_id = ?
        ''', (patient_id, room_id, start_date, end_date, allocation_id))
        self.conn.commit()

    def delete_allocation(self, allocation_id):
        self.c.execute('DELETE FROM RoomAllocation WHERE allocation_id = ?', (allocation_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
