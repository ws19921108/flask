#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template, session, redirect, url_for, request, send_from_directory
from flask_bootstrap import Bootstrap
from spider import getnews, getfund, getstock
from form import LoginForm
from flask_mail import Mail, Message
from config import ADMINS
import os
app = Flask(__name__)
app.config.from_object('config')



bootstrap = Bootstrap(app)
mail = Mail(app)

numbers = ['sh000300']
file1_url = None
file2_url = None
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
    global file1_url,file2_url
    if request.method == 'POST':
        for fileN in request.files:
                if fileN == 'file1':
                    file = request.files['file1']
                    if file and allowed_file(file.filename):
                        filename = file.filename
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        file1_url = url_for('uploaded_file', filename=filename)
                elif fileN == 'file2':
                    file = request.files['file2']
                    if file and allowed_file(file.filename):
                        filename = file.filename
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        file2_url = url_for('uploaded_file', filename=filename)
    return  render_template('face.html',file1_url=file1_url,file2_url=file2_url)

@app.route('/face/compare', methods=["POST"])
def compare():
    return 'conpare'

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
