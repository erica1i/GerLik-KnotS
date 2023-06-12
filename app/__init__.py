from flask import Flask, render_template, session, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)

# experience_dict = {'Programming Language': ['Excel', 'Python', 'Tableau', 'R', 'Bash', 'Powershell'],
#                     'Years of Experience (As of April 2022)': [8,4,3,2,1,1]}
# fig = px.bar(experience_dict, x='Programming Language',y='Years of Experience (As of April 2022)', color_discrete_sequence=['white'])
# fig.update_layout (
#     paper_bgcolor' : "rgba (0,0,0,0)"
#     # plot_bgcolor : "rgba (0,0,0,0)"
#     font_color = 'white',
#     font_family = ' verdana
#     font_size = 20,
# )


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
         user = User.query.filter_by(username=request.form['username']).first()
         if user:
             if user.password == request.form['password']:
                 session['username'] = request.form['username']
                 return redirect(url_for('dashboard'))
             else:
                 return render_template('login.html', message='Invalid login credentials')
         else:
             return render_template('login.html', message='Invalid login credentials')
     return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
     if request.method == 'POST':
         if User.query.filter_by(username=request.form['username']).first():
             return render_template('register.html', message='Username already exists')
         new_user = User(username=request.form['username'], password=request.form['password'])
         db.session.add(new_user)
         db.session.commit()
         return redirect(url_for('login'))
     return render_template('register.html')

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

@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)

    # Redirect the user to the login page
    return redirect(url_for('login'))

# @app.route('/report_expense', methods=['POST'])
# def report_expense():
#     # Get the form data
#     title = request.form.get('title')
#     cost = request.form.get('cost')
#     date = request.form.get('date')
#     category = request.form.get('category')

#     # TODO: Add the expense to the database

#     # Redirect the user back to the dashboard
#     return redirect(url_for('dashboard'))
@app.route('/report_expense', methods=['POST'])
def report_expense():
    # Get the form data
    title = request.form.get('title')
    cost = request.form.get('cost')
    date_str = request.form.get('date')
    category = request.form.get('category')

    # Convert the date string to a date object
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    # Get the current user
    user = User.query.filter_by(username=session['username']).first()

    # Create a new expense
    expense = Expense(title=title, cost=cost, date=date, category=category, user_id=user.id)

    # Add the expense to the database
    db.session.add(expense)
    db.session.commit()

    # Redirect the user back to the dashboard
    return redirect(url_for('dashboard'))

# @app.route('/report_expense', methods=['POST'])
# def report_expense():
#     # Get the form data
#     title = request.form.get('title')
#     cost = request.form.get('cost')
#     date = request.form.get('date')
#     category = request.form.get('category')

#     # Get the current user
#     user = User.query.filter_by(username=session['username']).first()

#     # Create a new expense
#     expense = Expense(title=title, cost=cost, date=date, category=category, user_id=user.id)

#     # Add the expense to the database
#     db.session.add(expense)
#     db.session.commit()

#     # Redirect the user back to the dashboard
#     return redirect(url_for('dashboard'))

@app.route('/chart', methods=['POST', 'GET'])
def chart():
    x=['b', 'a', 'c', 'd']
    fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
    fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
    fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.show()

#if __name__ == '__main__':
   # with app.app_context():
      #  db.create_all()
   # app.run(debug=True, port=5001)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(host = '0.0.0.0')
