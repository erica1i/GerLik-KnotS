import sqlite3

# def create_database():
#     conn = sqlite3.connect('expense_tracker.db')  # Creates a new database if not exists

#     c = conn.cursor()  # Create a cursor

#     # Create table - USERS
#     c.execute('''CREATE TABLE USERS
#                  ([generated_id] INTEGER PRIMARY KEY,[username] text, [password] text)''')

#     # Create table - EXPENSES
#     c.execute('''CREATE TABLE EXPENSES
#                  ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [expense] REAL, [category] TEXT, [date] TEXT)''')

#     # Create table - BUDGETS
#     c.execute('''CREATE TABLE BUDGETS
#                  ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [budget] REAL, [category] TEXT, [date] TEXT)''')

#     conn.commit()

#     print("SQLite database and tables created.")

# create_database()
# def create_database():
#     conn = sqlite3.connect('./instance/expense_tracker.db')  # Creates a new database if not exists

#     c = conn.cursor()  # Create a cursor

#     # Create table - USERS
#     c.execute('''CREATE TABLE USERS
#                  ([generated_id] INTEGER PRIMARY KEY,[username] text, [password] text)''')

#     # Create table - EXPENSES
#     c.execute('''CREATE TABLE EXPENSES
#                  ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [title] text, [expense] REAL, [category] TEXT, [date] TEXT)''')

#     # Create table - BUDGETS
#     c.execute('''CREATE TABLE BUDGETS
#                  ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [budget] REAL, [category] TEXT, [date] TEXT)''')

#     conn.commit()

#     print("SQLite database and tables created.")
from app import db, Expense

def create_all():
    conn = sqlite3.connect('expense_tracker.db')  # Creates a new database if not exists

    c = conn.cursor()  # Create a cursor

    # Check if table USERS exists and if not, create it
    c.execute('''CREATE TABLE IF NOT EXISTS USERS
                 ([generated_id] INTEGER PRIMARY KEY,[username] text, [password] text)''')

    # Check if table EXPENSES exists and if not, create it
    c.execute('''CREATE TABLE IF NOT EXISTS EXPENSES
                 ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [expense] REAL, [category] TEXT, [date] TEXT)''')

    # Check if table BUDGETS exists and if not, create it
    c.execute('''CREATE TABLE IF NOT EXISTS BUDGETS
                 ([generated_id] INTEGER PRIMARY KEY,[user_id] INTEGER, [budget] REAL, [category] TEXT, [date] TEXT)''')

    conn.commit()

    print("SQLite database and tables created.")


def create_database():
    db.create_all()
    print("SQLite database and tables created.")

def get_expenses_by_category(user_id):
    conn = sqlite3.connect('./instance/expense_tracker.db')
    c = conn.cursor()

    c.execute("SELECT category, SUM(expense) FROM EXPENSES WHERE user_id = ? GROUP BY category", (user_id,))

    data = c.fetchall()

    conn.close()

    return data


# create_database()
