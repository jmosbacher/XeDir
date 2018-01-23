from flask import Flask, render_template
from bokeh.embed import server_document
from subprocess import run, Popen
from time import sleep
bkpath = "/home/joe/Dropbox/Webapps/lab_status2"
BKPORT=5006
app = Flask(__name__)

@app.route('/')
def homepage():
    script = server_document('http://localhost:{}/lab_status2'.format(BKPORT))
    return render_template("plain.html", bkscript=script)

@app.route('/getting-started')
def about():
    return 'What about us?'

@app.route('/contact')
def contact():
    return 'First contact'

if __name__ == "__main__":
    Popen(['bokeh', 'serve', str(bkpath), '--port', str(BKPORT), '--allow-websocket-origin=localhost:5000','--allow-websocket-origin=localhost:{}'.format(BKPORT)])
    sleep(5)
    app.run()
