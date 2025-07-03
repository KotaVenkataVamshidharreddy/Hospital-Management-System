import sqlite3

class Medicine:
    def __init__(self):
        self.conn = sqlite3.connect('hospital_management.db')
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS Medicine (
            medicine_code INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        )''')
        self.conn.commit()

    def add_medicine(self, medicine_name, description, price):
        self.c.execute('INSERT INTO Medicine (medicine_name, description, price) VALUES (?, ?, ?)',
                       (medicine_name, description, price))
        self.conn.commit()

    def view_medicines(self):
        self.c.execute('SELECT * FROM Medicine')
        return self.c.fetchall()

    def update_medicine(self, medicine_code, medicine_name, description, price):
        self.c.execute('''
        UPDATE Medicine SET medicine_name = ?, description = ?, price = ? WHERE medicine_code = ?
        ''', (medicine_name, description, price, medicine_code))
        self.conn.commit()

    def delete_medicine(self, medicine_code):
        self.c.execute('DELETE FROM Medicine WHERE medicine_code = ?', (medicine_code,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
