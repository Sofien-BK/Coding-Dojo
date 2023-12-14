from flask_app import app
from flask import render_template , redirect , request , session ,  flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt= Bcrypt(app)

#! ====== Login / Register Page - View =======

@app.route("/")
def index():
    return render_template("index.html")

#? Register - Method -  Action 
@app.route("/users/register", methods=["post"])
def  user_register():
    if not User.validate(request.form):
        return redirect ("/")
    #! hash the  password
    pw_hashed = bcrypt.generate_password_hash(request.form["password"])
    #? get the data dict readu with the new hashe pw to create a User
    data = {**request.form, "password": pw_hashed  }
    #? save  user in DB
    user_id = User.create(data)
    session["user_id"] = user_id
    return redirect("/dashboard")
#? Login - method - action
@app.route("/users/login", methods=["post"])
def user_login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    # if email not found
    if not user_in_db:
        flash("Invalid credentials")
        return redirect("/")
    #now check  the password
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid credentials")
        return redirect("/")
    #* if all is  good
    session["user_id"] = user_in_db.id
    return redirect("/dashboard")
# display route dashbonard
@app.route("/dashboard")
def  dash():
    #! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data={"id": session["user_id"]}
    loggedin_user= User.get_user_by_id(data)
    return render_template('dashboard.html',loggedin_user = loggedin_user)

#! --------- Logout ------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")