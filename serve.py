from flask import Flask, render_template
from bokeh.embed import server_document

from time import sleep

BKSERVE='http://localhost:25006/lab_status'
app = Flask(__name__)

@app.route('/')
def homepage():
    script = server_document(BKSERVE)
    title='Cams and PMTs'
    return render_template("control.html", bkscript=script, title=title)

@app.route('/zen')
def zen():
    with open('zen.txt','r') as f:
        lines = list(f.readlines())
    return render_template("zen.html", lines=lines)

@app.route('/control')
def contact():
    return 'First contact'


if __name__ == "__main__":
    app.run()
