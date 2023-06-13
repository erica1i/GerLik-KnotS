from flask import Flask, session, jsonify, render_template, redirect, url_for, request as flask_request
import http.client
import sqlite3
import json
import os

DB_FILE = "expense_tracker.db"
db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT UNIQUE, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS expenses(username TEXT, expense REAL, title TEXT, category TEXT, date TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS budgets(username TEXT, budget REAL, title TEXT, category TEXT, date TEXT)''')

# def get_expenses_by_category(user_id):
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     c.execute("SELECT category, SUM(expense) FROM EXPENSES WHERE user_id = ? GROUP BY category", (user_id,))
#     data = c.fetchall()
#     db.close()
#     return data

def check_user_exist(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT username FROM users WHERE username=?", (username,))
    user = c.fetchone()
    db.close()
    return user!= None

def get_password(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    pw = c.fetchone()
    db.close()
    return pw[0]

def new_user(new_account):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", new_account)
    db.commit()
    db.close()

def get_users():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    userlist = c.execute("SELECT username from users;").fetchall()
    db.commit()
    db.close()
    return userlist

def get_combo():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    combolist = c.execute("SELECT username, password from users;").fetchall()
    db.commit()
    db.close()
    return combolist

def new_user(new_account):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", new_account)
    db.commit()
    db.close()

def change_pw(username, new_pw):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE users SET password = ? WHERE username=?", (new_pw, username))
    db.commit()
    db.close()

def import_expense(stored_data):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("insert into expenses values (?,?,?,?,?);", stored_data)
    db.commit()
    db.close()

def import_budgets(stored_data):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("insert into budgets values (?,?,?,?,?);", stored_data)
    db.commit()
    db.close()

def get_expense(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT category, expense, title, date FROM expenses WHERE username = ?", (username,))
    data = c.fetchall()
    db.commit()
    db.close()
    return data
