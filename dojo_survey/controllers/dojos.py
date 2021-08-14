from dojo_survey import app
from flask import render_template,redirect,request,session,flash
from dojo_survey.models.dojo import Friend


@app.route('/')  
def index(): 
    if 'tracker' not in session:
        session['tracker'] = 0
    return render_template("index.html") 

@app.route('/results', methods=['POST'])  
def results():

    if not Friend.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things

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