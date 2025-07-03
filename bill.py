import sqlite3

class Bill:
    def __init__(self, db_name='hospital_management.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Bill (
            bid INTEGER PRIMARY KEY AUTOINCREMENT,
            pid INTEGER,
            treatment TEXT,
            medicine_code INTEGER,
            medicine_name TEXT,
            quantity INTEGER,
            price REAL,
            FOREIGN KEY (pid) REFERENCES Patient(pid) ON DELETE CASCADE
        )''')
        self.conn.commit()

    def add_bill(self, pid, treatment, medicine_code, medicine_name, quantity, price):
        self.c.execute('INSERT INTO Bill (pid, treatment, medicine_code, medicine_name, quantity, price) VALUES (?, ?, ?, ?, ?, ?)',
                       (pid, treatment, medicine_code, medicine_name, quantity, price))
        self.conn.commit()

    def view_bills(self):
        self.c.execute('SELECT * FROM Bill')
        return self.c.fetchall()

    def update_bill(self, bid, pid, treatment, medicine_code, medicine_name, quantity, price):
        self.c.execute('''UPDATE Bill SET pid = ?, treatment = ?, medicine_code = ?, medicine_name = ?, quantity = ?, price = ? WHERE bid = ?''',
                       (pid, treatment, medicine_code, medicine_name, quantity, price, bid))
        self.conn.commit()

    def delete_bill(self, bid):
        self.c.execute('DELETE FROM Bill WHERE bid = ?', (bid,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
