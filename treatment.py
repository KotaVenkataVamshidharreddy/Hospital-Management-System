import sqlite3

class Treatment:
    def __init__(self):
        self.conn = sqlite3.connect('hospital_management.db')
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS Treatment (
            treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            treatment_name TEXT NOT NULL,
            description TEXT,
            cost REAL NOT NULL
        )''')
        self.conn.commit()

    def add_treatment(self, treatment_name, description, cost):
        self.c.execute('INSERT INTO Treatment (treatment_name, description, cost) VALUES (?, ?, ?)',
                       (treatment_name, description, cost))
        self.conn.commit()

    def view_treatments(self):
        self.c.execute('SELECT * FROM Treatment')
        return self.c.fetchall()

    def update_treatment(self, treatment_id, treatment_name, description, cost):
        self.c.execute('''
        UPDATE Treatment SET treatment_name = ?, description = ?, cost = ? WHERE treatment_id = ?
        ''', (treatment_name, description, cost, treatment_id))
        self.conn.commit()

    def delete_treatment(self, treatment_id):
        self.c.execute('DELETE FROM Treatment WHERE treatment_id = ?', (treatment_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
