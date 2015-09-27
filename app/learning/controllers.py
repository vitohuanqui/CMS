from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for
)
from app.learning.forms import TextForm

mod_learn = Blueprint('learn', __name__, url_prefix='/learn')

@mod_learn.route('/hello/')
def hello_world():
    return 'Hello World!'

@mod_learn.route('/something/', methods=['GET', 'POST'])
def someting():
    form = TextForm(request.form)
    if form.validate_on_submit():
        text = form.text.data
        if text:
            return text
        else:
            return "vacio"

    return render_template("learning/learn.html", form=form)
