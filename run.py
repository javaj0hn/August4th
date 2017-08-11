#!/usr/bin/env python
from flask import Flask, request, redirect, url_for, send_from_directory, abort, render_template

# Import Configuration
from conf import config

# Import Project Files
from August4th import db
#from August4th import application

app = Flask(__name__)

# Functions


# Routes
'''
Index Page
Allow multiple image & file uploads
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = dict()
        file = request.files['file']

        if file and whiteList(file.filename):
            filename = secure_filename(file.filename)
            while os.path.exists(os.path.join(config["UPLOAD_FOLDER"], filename)):
                filename = str(randint(1000,8999)) + '-' + secure_filename(filename)
            db.uploadFile(filename)
            file.save(os.path.join(config['UPLOAD_FOLDER'], filename))
            data["file"] = filename
            data["url"] = config["DOMAIN"] + "/" + filename

            try:
                if request.form["source"] == "web":
                    return render_template('link.html', data=data, page=config["SITE_DATA"])
            except Exception as e:
                return json.dumps(data)
        else:
            return errorPage(error="This file is not allowed.", code=403)

    elif request.method == 'GET':
        return render_template('index.html', page=config["SITE_DATA"])
    return render_template('index.html')

'''
Pastebin Page
'''
@app.route('/paste', methods=['GET', 'POST'])
def paste():
    if request.method == 'POST' and request.form['code']:
        #db call function
        #Generate random ID
        ID = 1
        content = "hello"
        pType = "PHP"
        db.add_paste(ID, content, pType)
        return redirect(url_for('showPaste', ID=ID))
    return render_template('paste.html')

'''
Show Paste
'''
@app.route('/paste/<int:pid>', methods=['GET')
def showPaste(pid):
    db.getPaste(pid)
    return render_template('pasteResults.html')

if __name__ == '__main__':
  app.run(
    port=config["PORT"],
    host=config["HOST"],
    debug=config["DEBUG"]
  )
