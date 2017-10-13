#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template, session, redirect, url_for, request, send_from_directory
from flask_bootstrap import Bootstrap
from spider import getnews, getfund, getstock
from form import LoginForm, UploadForm1, UploadForm2, CompareForm
from flask_mail import Mail, Message
from config import ADMINS
import os
import json
import requests

app = Flask(__name__)
app.config.from_object('config')



bootstrap = Bootstrap(app)
mail = Mail(app)

numbers = ['sh000300']

file_url1 = None
file_url2 = None
face_token1 = None
face_token2 = None
confidence = None
# with app.app_context():
#     # within this block, current_app points to app.
#     msg = Message('test flask', sender=ADMINS[0], recipients=ADMINS)
#     msg.body = 'text body'
#     msg.html = '<b>HTML</b> body'
#     mail.send(msg)





@app.route('/')
def index():
    return render_template('index.html', numbers=numbers, news=getnews(), funddatas=getfund('160215'), stockdatas=getstock('sh000001'))
@app.route('/404')
def error():
    return render_template('404.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/onenet')
def onenet():
    return render_template('onenet.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
@app.route('/face', methods=['GET', 'POST'])
def face():
    global file_url1, file_url2, face_token1, face_token2, confidence
    uploadForm1 = UploadForm1()
    uploadForm2 = UploadForm2()
    compareForm = CompareForm()
    if request.method=='POST':
        if uploadForm1.submit1.data or uploadForm2.submit2.data:
            file = request.files['upFile']
            if file and allowed_file(file.filename):
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
                files = {'image_file': open(filepath, 'rb')}
                payload = {
                    'api_key': 'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB',
                    'api_secret': 'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV',
                }

                req = requests.post(url=url, files=files, data=payload)
                data = json.loads(req.text)
                face_token = data['faces'][0]['face_token']
                file_url = url_for('uploaded_file', filename=filename)

                if uploadForm1.submit1.data:
                    file_url1 = file_url
                    face_token1 = face_token
                if uploadForm2.submit2.data:
                    file_url2 = file_url
                    face_token2 = face_token
        if compareForm.submitCompare.data:
            url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
            payload = {
                'api_key': 'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB',
                'api_secret': 'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV',
                'face_token1':face_token1,
                'face_token2': face_token2,
            }
            req = requests.post(url=url, data=payload)
            data = json.loads(req.text)

            confidence = data['confidence']

    return  render_template('face.html',uploadForm1=uploadForm1,uploadForm2=uploadForm2,compareForm=compareForm,
                            file_url1=file_url1,file_url2=file_url2,face_token1=face_token1,
                            face_token2=face_token2,confidence=confidence)

@app.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['HasLogin'] = True
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
@app.route('/logout')
def logout():
    session['HasLogin'] = False
    return render_template('logout.html')

if __name__ == '__main__':
    app.run()
