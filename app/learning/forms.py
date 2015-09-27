from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import validators 


class TextForm(Form):
    text    = TextField('Some text', [validators.Length(max=25)])
