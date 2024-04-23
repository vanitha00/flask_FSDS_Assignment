###basic flask questions
# Basics of Flask:
#1. Create a Flask app that displays "Hello, World!" on the homepage.

from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "HELLO WORLD!"
if __name__=='__main__':
    app.run(debug=True)

#2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return("pwskills")
@app.route("/student")
def student():
    return render_template('student.html')
@app.teacher('/teacher')
def teacher():
    return render_template('teacher.html')

#3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask,render_template,request,Response,url_for,redirect
app=Flask(__name__)
@app.route('/')
def home():
    return "vanitha kotla"
@app.route('/marks/<int:score>')
def marks(score):
    return f"your score {score}"
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        cd=int(request.form['cd'])
        dsp=int(request.form['dsp'])
        sum=cd+dsp
        return redirect(url_for('marks',score=sum))
    return render_template('flask_vanitha_waste.html')
if __name__=='__main__':
    app.run(debug=True)

#4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)
@app.route('/')
def home(user):
    return f'USER_NAME{user}'
@app.route("/form_details",method=['POST','GET']) 
def form_details():
    if request.method=='POST':
        user_name=request.form['user']
        return redirect(url_for('home',user=user_name))
    return render_template('Flask_FSDCPRO.html')

if __name__=='__main__':
    app.run(debug=True)

#5.Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask,render_template,request,url_for,redirect,session
app=Flask(__name__)
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % session['username']
    return 'you are not logged in'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='post':
        session['username']=request.form['username']
        return redirect(url_for('index'))
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)


