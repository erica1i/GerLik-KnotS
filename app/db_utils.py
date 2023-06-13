import sqlite3
from flask import session

def get_expenses_by_category(user_id):
    # user_id = session.get('user_id')
    user_id = get_user_id_by_username(session.get('username'))
    conn = sqlite3.connect('./instance/expense_tracker.db')
    c = conn.cursor()

    c.execute("SELECT category, SUM(expense) FROM EXPENSES WHERE user_id = ? GROUP BY category", (user_id,))

    data = c.fetchall()

    conn.close()

    return data

def get_user_id_by_username(username):
    # conn = sqlite3.connect('expense_tracker.db')
    conn = sqlite3.connect('./instance/expense_tracker.db')
    c = conn.cursor()

    c.execute('SELECT id FROM user WHERE username = ? LIMIT 1', (username,))
    user_id = c.fetchall()[0][0]#c.fetchone()[0] if c.fetchone() else None

    conn.close()

    return user_id