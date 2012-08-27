from flask import Flask
from flask import json
from flask import request
from flask import render_template, flash, redirect, url_for, escape, session
import psycopg2
from flask.ext.sqlalchemy import SQLAlchemy
from forms import SigninForm, RegistrationForm
from werkzeug import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(200))
    uptime = db.Column(db.String(200))
    hostname = db.Column(db.String(20))
    flagger = db.Column(db.Boolean)

    def __init__(self, time, uptime, hostname, flagger):
        self.time = time
        self.uptime = uptime
        self.hostname = hostname
        self.flagger = flagger

    def __repr__(self):
        return '<Log %r>' % (self.hostname)

    def delete_all_logs(self):
        my_log = Log.query.all()
        for l in my_log:
            db.session.delete(l)
        db.session.commit()


db.create_all()


@app.route('/')
@app.route('/index')
def index():
    # shit got real
    if 'username' in session:
        user = User.query.filter_by(username=escape(session['username'])).first()
        log = Log.query.all()
        status = Log.query.order_by('-id').first()
        return render_template('index.html', title='OMG', user=user, log=log,
                                                            status=status)
    else:
        username = None
        user = None
        log = None
        status = None
        return render_template('index.html', title='OMG', user=user, log=log,
                                                            status=status)


@app.route('/logger', methods=['POST'])
def api_recieve():
    if request.headers['Content-type'] == 'application/json':
        return "JSON message: " + json.dumps(request.json)
    else:
        return "415 not supported Content-Type"


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration form
    """

    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data,
                        generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        session['username'] = user.username
        # flash will display a message to the user
        flash('Thanks for registering')
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('index'))
    return render_template("forms/register.html", form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    signin form
    """

    error = None
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            session['username'] = user.username
            flash('welcome %s' % user.username)
            return redirect(url_for('index'))
        else:
            error = 'wrong combination username/password'
            flash(error)

    return render_template("forms/signin.html", title='Sign in',
                                                form=form, error=error)


@app.route('/signout')
def signout():
    """
    signout
    """
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    # quitar el debug despeus
    app.run(host='0.0.0.0', debug=True)
