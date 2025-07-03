import sqlite3

class Room:
    def __init__(self, db_name='hospital_management.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Room (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            room_type TEXT NOT NULL,
            period TEXT NOT NULL
        )''')
        self.conn.commit()

    def add_room(self, room_type, period):
        self.c.execute('INSERT INTO Room (room_type, period) VALUES (?, ?)', 
                       (room_type, period))
        self.conn.commit()

    def view_rooms(self):
        self.c.execute('SELECT * FROM Room')
        return self.c.fetchall()

    def update_room(self, rid, room_type, period):
        self.c.execute('''UPDATE Room SET room_type = ?, period = ? WHERE rid = ?''', 
                       (room_type, period, rid))
        self.conn.commit()

    def delete_room(self, rid):
        self.c.execute('DELETE FROM Room WHERE rid = ?', (rid,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
