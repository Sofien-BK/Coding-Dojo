from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "everybody want to live together"


@app.route("/")
def display():
    if "visit" in session:
        session["visit"] += 1
    else:
        session["visit"] = 1
    return render_template("counter.html", visit_counter=session["visit"])
@app.route('/count')
def clicking ():
    if "visit" in session:
        session["visit"] += 1
    return render_template("counter.html", visit_counter=session["visit"])
@app.route('/reset')
def reseting():
    if "visit" in session:
        session.pop("visit")
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
