import sqlite3

users = sqlite3.connect("users.db")
cursor = users.cursor()

def check_password(username, password):
    cursor.execute("SELECT Password FROM Users WHERE Username = ?", (username,))
    correct_password = cursor.fetchone()
    if correct_password != None:
        correct_password = correct_password[0]

    if correct_password == password:
        return True
    else:
        return False

def make_account(username, password):
    cursor.execute("SELECT Password FROM Users WHERE Username = ?", (username,))
    temp = cursor.fetchone()

    if temp != None:
        return False
    else:
        cursor.execute("SELECT COUNT(*)")
        ID = cursor.fetchone()[0]
        cursor.execute("INSERT INTO Users VALUES (?, ?, ?)", (ID, username, password))
        return True