import os
from flask import Flask, render_template
from form import NameForm

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

app.config['SECRET_KEY'] = 'ja;sdlkfj;asdlkfja;sdlfkjas;lkdfja;slkdfj'

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
    return render_template('index.html', name=name, form=form)  # Corrigida a indentação