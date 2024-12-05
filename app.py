import os
from flask import Flask, render_template

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder = template_dir)

@app.route('/user')
@app.route('/user/<name>')
def index(name=None):
    print(name)
    return render_template('index.html', name=name)