from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route(
    "/"
)  # The "@" decorator associates this route with the function immediately following
def get_all_dojos():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("home.html", dojos=all_dojos)


# * DISPLAY ROUTE - RENDER
# @app.route(
#     "/form"
# )  # The "@" decorator associates this route with the function immediately following
# def display_form():
#     return render_template("form.html")


#! ACTION ROUTE - CREATE
@app.route(
    "/create", methods=["POST"]
)  # The "@" decorator associates this route with the function immediately following
def create_dojo():
    # print(request.form)
    user_dict = {**request.form}
    Ninja.create_quote(user_dict)
    return redirect("/")

# * DISPLAY ROUTE NINJA - RENDER
@app.route("/ninjas")
def create_ninja():
    dojos=Dojo.get_all()
    return render_template("create_ninja.html",dojos=dojos)



# * DISPLAY ROUTE - RENDER
@app.route("/show/<int:id>")
def show_one(id):
    data = {"id": id}
    dojo = Dojo.get_one(data)
    return render_template("table.html", dojo=dojo)


# # * DISPLAY ROUTE - RENDER
# @app.route("/edit/<int:id>")
# def update_user(id):
#     user_id_dict = {"id": id}
#     user = Dojo.get_one(user_id_dict)
#     return render_template("edit.html", user=user)


# #! ACTION ROUTE
# @app.route("/update/<int:id>", methods=["POST"])
# def process_update(id):
#     data = {
#         **request.form,
#         "id": id,
#     }
#     Dojo.update(data)
#     return redirect("/")