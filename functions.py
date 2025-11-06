import sqlite3

users = sqlite3.connect("users.db")
cursor = users.cursor()

def check_password(username, password):
    cursor.execute("SELECT Password FROM Users WHERE Username = ?", (username,))
    correct_password = cursor.fetchone()
    correct_password = correct_password[0]

    if correct_password == password:
        return True
    else:
        return False

def make_account():
    pass