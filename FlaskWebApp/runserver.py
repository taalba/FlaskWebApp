"""
This script runs the FlaskWebApp application using a development server.
"""
from subprocess import call

import time
time.sleep(20)

call(["python", "data/generateModel.py"])
call(["python", "data/generateData.py"])

from os import environ
from FlaskWebApp import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
