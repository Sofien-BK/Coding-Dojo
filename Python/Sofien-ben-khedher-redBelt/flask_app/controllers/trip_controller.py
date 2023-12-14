from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.trip_model import Trips


# * ==================== Display dashboard ====================
@app.route("/dashboard")
def display_recipes():
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    trips_list = Trips.get_all_for_user(data)
    return render_template(
        "dashboard.html", loggedin_user=loggedin_user, trips_list=trips_list 
    )


# * ==================== Display New Trip ====================
@app.route("/trips/new")
def new_trip():
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    return render_template("add_trip.html" , loggedin_user=loggedin_user)


# * ==================== Create New trip ====================
@app.route("/create/trip", methods=["post"])
def create():
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    if not Trips.validate(request.form):
        return redirect("/trips/new")
    data = {
        **request.form,
        "user_id": int(session["user_id"]),
    }
    new_trip = Trips.create_trip(data)
    print(new_trip)
    return redirect("/dashboard")


# # * ==================== Trip Content ====================
@app.route("/trips/<int:id>")
def trip_cnt(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    trip = Trips.get_by_id({"id": id})
    if trip:
        trip_des = trip.destination
        cnt = {
            "Start Date": trip.start_date,
            "End Date": trip.end_date,
            "Created On": trip.created_at,
            "Last Updated": trip.updated_at,
            "Plan": trip.plan,
            "Created By": trip.poster.first_name
        }
    print(cnt)
    return render_template(
        "trip_content.html",
        trip=trip,
        loggedin_user=loggedin_user,
        trip_des=trip_des,
        cnt=cnt,
    )


# # * ==================== Trip - Edit -  display ====================
@app.route("/trips/edit/<int:id>")
def edit_trip(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    trip = Trips.get_by_id({"id": id})
    if trip:
        trip_des = trip.destination
        trip_st = trip.start_date
        trip_ed = trip.end_date
        trip_pl = trip.plan
        tripId = trip.id
    return render_template(
        "edit_trip.html", trip_des=trip_des, trip_st=trip_st, trip_ed=trip_ed, trip_pl=trip_pl , loggedin_user=loggedin_user , tripId = tripId
    )


# # * ==================== Recipes - Edit - Action ====================
@app.route("/edit/<id>", methods=["post"])
def editing(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    if not Trips.validate(request.form):
        return redirect("/trips/edit/"+id)
    elif Trips.validate(request.form):
        data = {
            **request.form,
            "user_id": int(session["user_id"]),
            "id" : id
        }
        print(data)
        Trips.edit(data)
        return redirect("/dashboard")

# # * ==================== Delete Recipe ====================
@app.route("/delete/<int:id>")
def delete(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    Trips.delete({'id':id})
    return redirect("/dashboard")