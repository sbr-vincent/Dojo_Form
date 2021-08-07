from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)    
app.secret_key = 'Mellon'


@app.route('/')  
def index(): 
    if 'tracker' not in session:
        session['tracker'] = 0
    return render_template("index.html") 

@app.route('/results', methods=['POST'])  
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/display") 

@app.route('/display')  
def display():
    session['tracker'] = 1
    return render_template("index.html")

@app.route('/destroy_session', methods=['POST'])  
def restart():
    session['tracker'] = 0
    session.clear()
    return redirect("/") 

if __name__=="__main__":    
    app.run(debug=True)   