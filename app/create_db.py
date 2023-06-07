import sqlite3

def create_database():
    conn = sqlite3.connect('expense_tracker.db')  # Creates a new database if not exists

    c = conn.cursor()  # Create a cursor

    # Create table - USERS
    c.execute('''CREATE TABLE USERS
                 ([generated_id] INTEGER PRIMARY KEY,[username] text, [password] text)''')

    # Create table - EXPENSES
    c.execute('''CREATE TABLE EXPENSES
                 ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [expense] REAL, [category] TEXT, [date] TEXT)''')

    # Create table - BUDGETS
    c.execute('''CREATE TABLE BUDGETS
                 ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [budget] REAL, [category] TEXT, [date] TEXT)''')

    conn.commit()

    print("SQLite database and tables created.")

create_database()
