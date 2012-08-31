from flask.ext.wtf import Form, TextField, PasswordField
from flask.ext.wtf import Required, Email, EqualTo


class SigninForm(Form):
    """ docstring for LoginForm """

    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])


class RegistrationForm(Form):
    """docstring for RegistrationForm"""

    username = TextField('Username', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm = PasswordField('Confirm password', validators=[Required(),
                          EqualTo('confirm', message='Passwords must match')])


class EditUserForm(Form):
    """docstring for EditUserForm"""

    username = TextField('Username', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm = PasswordField('Confirm password', validators=[Required(),
                          EqualTo('confirm', message='Passwords must match')])
