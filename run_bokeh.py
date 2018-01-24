from subprocess import run, Popen
bkpath = "/home/joe/Dropbox/Webapps/lab_status2"
if __name__ == "__main__":
    Popen(['bokeh', 'serve', str(bkpath), '--port', str(BKPORT), '--allow-websocket-origin=localhost:5000','--allow-websocket-origin=localhost:{}'.format(BKPORT)])
    sleep(5)
