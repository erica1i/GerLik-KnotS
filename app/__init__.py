from flask import Flask, render_template, session, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
app.config['SECRET_KEY'] = 'cd85d99372e02261cc7fb70ef9b1ddfc'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    expense = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/login", methods =['GET', 'POST'])
def authenticate():
    user = request.form['username']
    passw = request.form['password']
    #print(db.valid_login(user, passw))
    
    if db.valid_login(user, passw):
        session['username'] = user
        return render_template('home.html', msg = "successfully logged in")
    else:
        return render_template('login.html', msg="Login Failed")

@app.route("/register", methods=['GET','POST'])
def register_account():
    if 'username' in session: #if someone tries to register while already logged in
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['newUser']
    #user = request.form.get('newUser')
    passw = request.form['newPass']
    #passw = request.form.get('newPass')
    passw2 = request.form['confirmPass']

    if not passw == passw2: #checks if the password matches the confirmation password
        return render_template("register.html", FAILMSG="Passwords don't match!")
       
    if db.user_exists(user):
        return render_template('register.html', FAILMSG="Username is in use!")
    else:
        db.add_user(user, passw)
        return render_template('login.html', FAILMSG = "User registered!, Log in with your new credentials.")

@app.route("/logout", methods=['GET', 'POST'])
def log_out():
    session.pop('username', None)
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session.get('username'))
    else:
        return redirect(url_for('login'))

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
