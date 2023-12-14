from flask import Flask , render_template , redirect , request , session
app = Flask(__name__)
app.secret_key = "everybody want to live together"
@app.route('/')
def survey ():
    return render_template('dojo_survey.html')
@app.route('/process' , methods = ['post'])
def save():
    user_data= {"name": request.form["name"],
                "location": request.form["location"],
                "language": request.form["language"],
                "comment": request.form["comment"],}
                
    session['user_dict'] = user_data
    print(session['user_dict'])
    return redirect('/result')
@app.route('/result')
def result(): 
    db = session['user_dict']
    return render_template ('submit.html' , db=db  )
    






if __name__=="__main__":
    app.run(debug=True)