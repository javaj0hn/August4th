#!/usr/bin/env python
from flask import Flask, request, redirect, url_for, send_from_directory, abort, render_template

# Import Configuration
from conf import config

# Import Project Files
from August4th import db
from August4th.output import print_log, time_to_string
from August4th import application

app = Flask(__name__)

# Functions


# Routes
'''
Index Page
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

'''
Pastebin Page
'''
@app.route('/paste', methods=['GET', 'POST'])
def paste():
    return render_template('paste.html')

if __name__ == '__main__':
  app.run(
    port=config["PORT"],
    host=config["HOST"],
    debug=config["DEBUG"]
  )
