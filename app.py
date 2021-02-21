from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost/lexus"
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://eojxzvvalovlxd:11d9ead423e58a8efd96e32203292c2b8ceb3d7e79e99026f80785cf54c32d1c@ec2-34-194-215-27.compute-1.amazonaws.com:5432/d3jf0gjk2e7u4d"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/')
def index():
    return render_template('index.htm')


@app.route('/admin')
def admin():
    rows = User.query.all()
    return render_template('admin.htm', data=rows)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    if(name == '' or email == ''):
        # return render_template('index.htm', message="Enter the necessary fields")
        flash("Enter the necessary fields", category='message')
        flash("You are redirected", category='message')
        return redirect('/')
    else:
        print(name, email)
        data = User(name, email)
        try:
            db.session.add(data)
            db.session.commit()
            send_mail(name, email)
            return render_template('success.htm')

        except:
            flash("You've already responded")
            return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'

    app.run()
