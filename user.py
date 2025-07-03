import sqlite3
import hashlib

class User:
    def __init__(self, db_name='hospital_management.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS User (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )''')
        self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password, role):
        if len(password) <= 6:
            print("Password must be greater than 6 characters.")
            return
        
        hashed_password = self.hash_password(password)
        try:
            self.c.execute('INSERT INTO User (username, password, role) VALUES (?, ?, ?)',
                           (username, hashed_password, role))
            self.conn.commit()
            print("User registered successfully!")
        except sqlite3.IntegrityError:
            print("Username already exists. Please try a different one.")

    def login(self, username, password):
        hashed_password = self.hash_password(password)
        self.c.execute('SELECT * FROM User WHERE username = ? AND password = ?', (username, hashed_password))
        user = self.c.fetchone()
        if user:
            print("Login successful!")
            return user
        else:
            print("Invalid credentials.")
            return None

    def close_connection(self):
        self.conn.close()
