from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipes import Recipes


# * ==================== Display Recipes ====================
@app.route("/recipes")
def display_recipes():
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    rerecipes = Recipes.get_all()
    rec_list = []
    for recipe in rerecipes:
        if recipe.under == 0:
            recipe.under = "No"
        elif recipe.under == 1:
            recipe.under = "Yes"
        all_rec = [
            recipe.name,
            recipe.under,
            recipe.poster.name,
            recipe.id,
            recipe.user_id,
        ]
        rec_list.append(all_rec)
        print(all_rec)
    return render_template(
        "recipes.html", loggedin_user=loggedin_user, rec_list=rec_list, recipe=recipe
    )


# * ==================== Display New Recipes ====================
@app.route("/recipes/new")
def new_recipes():
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    return render_template("new_recipes.html")


# * ==================== Create New Recipes ====================
@app.route("/create/recepie", methods=["post"])
def create():
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    if not Recipes.validate(request.form):
        return redirect("/recipes/new")
    data = {
        **request.form,
        "user_id": int(session["user_id"]),
    }
    new_recipe = Recipes.create_recipe(data)
    print(new_recipe)
    return redirect("/recipes")


# * ==================== Recipes Content ====================
@app.route("/recipes/<int:id>")
def recipe_cnt(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    recipe = Recipes.get_by_id({"id": id})
    if recipe:
        recipe_name = recipe.name
        poster = recipe.poster.name
        cnt = {
            "Description": recipe.descreption,
            "Under 30 minutes ?": recipe.under,
            "Instructions": recipe.instructions,
            "Date Mode": recipe.date,
        }
    if cnt["Under 30 minutes ?"] == 0:
        cnt["Under 30 minutes ?"] = "No"
    else:
        cnt["Under 30 minutes ?"] = "Yes"
    print(cnt)
    return render_template(
        "recipe_cnt.html",
        recipe=recipe,
        loggedin_user=loggedin_user,
        recipe_name=recipe_name,
        poster=poster,
        cnt=cnt,
    )


# * ==================== Recipes - Edit -  display ====================
@app.route("/recipes/<int:id>/edit")
def edit(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    recipe = Recipes.get_by_id({"id": id})
    if recipe:
        recipe_name = recipe.name
        des = recipe.descreption
        ints = recipe.instructions
        dt = recipe.date
        rec_id = recipe.id
    return render_template(
        "recipe_edit.html", recipe_name=recipe_name, des=des, ints=ints, dt=dt , rec_id = rec_id
    )


# * ==================== Recipes - Edit - Action ====================
@app.route("/editing/<int:id>", methods=["post"])
def editing(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    if not Recipes.validate(request.form):
        return redirect("/recipes/new")
    elif Recipes.validate(request.form):
        data = {
            **request.form,
            "user_id": int(session["user_id"]),
            "id" : id
        }
        print(data)
        Recipes.edit(data)
        return redirect("/recipes")

# * ==================== Delete Recipe ====================
@app.route("/delete/<int:id>")
def delete(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    Recipes.delete({'id':id})
    return redirect("/recipes")