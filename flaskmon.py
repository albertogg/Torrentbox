from flask import Flask
from flask import json
from flask import request
import psycopg2
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask_app'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(25))
    uptime = db.Column(db.String(200))
    hostname = db.Column(db.String(20))
    uname = db.Column(db.String(20))
    flagger = db.Column(db.Boolean)

    def __init__(self, time, uptime, hostname, uname, flagger):
        self.time = time
        self.uptime = uptime
        self.hostname = hostname
        self.uname = uname
        self.flagger = flagger

    def __repr__(self):
        return '<Log %r>' % (self.hostname)

    def delete_all_logs(self):
        my_log = Log.query.all()
        for l in my_log:
            db.session.delete(l)
        db.session.commit()


db.create_all()


@app.route("/")
def hello():
    # return "Hello World!"
    user = User.query.all()
    return '%r' % user


@app.route('/logger', methods=['POST'])
def api_recieve():
    if request.headers['Content-type'] == 'application/json':
        return "JSON message: " + json.dumps(request.json)
    else:
        return "415 not supported Content-Type"

if __name__ == "__main__":
    app.run(debug=True)
