from app import app
from flask import Flask, render_template, request,url_for,redirect
from werkzeug.utils import secure_filename
import os
import urllib.request

@app.route('/')
@app.route('/upload',methods=['POST','GET'])
def upload_file():
   return render_template('index.html')

@app.route('/uploader',methods=['POST'])
def uploader_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return render_template('index.html', filename=filename)
@app.route('/display<filename>')
def display_image(filename):
    filename = 'http://127.0.0.1:5000/static/uploads/' + filename
    return render_template('template.html',filename=filename)
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

#if __name__ == '__main__':
  # app.run(debug = True)set FLASK_APP=display.py