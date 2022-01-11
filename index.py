from flask import Flask

import os, sys
app = Flask(__name__)

@app.route('/hello')
def get_basic():
    return f"Hello World, Served from {os.getpid()}"

port = 8822
if sys.argv.__len__() > 1:
    port = sys.argv[1]

app.run(port=port)